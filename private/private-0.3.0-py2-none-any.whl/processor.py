import base64
import codecs
import hashlib
import logging
import os
import re
import shutil
import tempfile
import zipfile
import zlib

import pyaes
import six

try:
    import astunparse
except ImportError:
    astunparse = None

from . import source_tags
from . import packages


MODULE_TEMPLATE = os.path.join(os.path.dirname(__file__), "module_template.txt")
KEY_SIZE = 16
MAX_LINE_LENGTH = 80

template = None

logger = logging.getLogger(__name__)


def _chunks(data, chunk_size):
    """Returns generator that yields chunks of chunk size of data"""
    return (data[i : i + chunk_size] for i in range(0, len(data), chunk_size))


def process_module(module_path, output_path, action_list):
    """Encrypts python file with into output path"""

    with open(module_path, "r") as module_file:
        module_content = module_file.read()

    namespace = {"source": module_content}
    for action, input, output in action_list:
        input = [namespace[name] for name in input]
        action_output = action(*input)
        namespace[output] = action_output

    with open(output_path, "w") as output_file:
        output_file.write(namespace["source"])

    logger.debug("Encrypted file {} into {}".format(module_path, output_path))


def template_encrypted_code(encrypted_code, code_hash):
    encrypted_code = codecs.decode(encrypted_code)

    global template
    if template is None:
        with open(MODULE_TEMPLATE, "r") as template_file:
            template = template_file.read()

    encrypted_code = os.linesep + os.linesep.join(_chunks(encrypted_code, MAX_LINE_LENGTH))
    return template.format(module_name=__package__, encryped_code=encrypted_code, code_hash=code_hash)


def process_directory(input_directory, output_directory, action_list):
    for root, _, files in os.walk(input_directory):
        encrypted_path = os.path.join(output_directory, os.path.relpath(root, input_directory))

        if not os.path.exists(encrypted_path):
            os.makedirs(encrypted_path)

        for file_name in files:
            source_file = os.path.join(root, file_name)
            destionation_file = os.path.join(encrypted_path, file_name)
            if file_name.endswith(".py"):
                process_module(source_file, destionation_file, action_list)
            else:
                shutil.copy2(source_file, destionation_file)
                logger.debug("Copying {} to {}".format(source_file, destionation_file))


def _generate_record_file(directory):
    records = set()
    for root, _, files in os.walk(directory):
        for current_file_name in files:
            if current_file_name == "RECORD":
                continue
            current_file_path = os.path.join(root, current_file_name)
            with open(current_file_path, "r") as current_file:
                file_content = current_file.read()
            file_hash = hashlib.sha256(file_content).digest()
            record = [
                os.path.relpath(current_file_path, directory),
                "sha256=" + base64.urlsafe_b64encode(file_hash).replace("=", ""),
                str(len(file_content)),
            ]
            records.add(",".join(record))
    return "\n".join(records)


def process_wheel(wheel_path, output_dir, action_list):
    """Encrypts wheel package with key into output directory"""
    unzipped_dir = tempfile.mkdtemp()
    encrypted_dir = tempfile.mkdtemp()
    with zipfile.ZipFile(wheel_path, "r") as wheel_file:
        wheel_file.extractall(unzipped_dir)

    logger.info("Encrypting wheel {}".format(wheel_path))
    process_directory(unzipped_dir, encrypted_dir, action_list)

    record_content = _generate_record_file(encrypted_dir)
    (dist_info_directory,) = [
        path for path in os.listdir(encrypted_dir) if re.match(".*\.dist-info", path)
    ]
    record_file_path = os.path.join(dist_info_directory, "RECORD")
    logger.info("Rewriting " + record_file_path)
    record_content += "\n{},,".format(record_file_path)
    with open(os.path.join(encrypted_dir, record_file_path), "w") as record_file:
        record_file.write(record_content)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    output_path = os.path.join(output_dir, os.path.basename(wheel_path))
    shutil.make_archive(output_path, "zip", root_dir=encrypted_dir)
    os.rename(output_path + ".zip", output_path)


def process_paths(paths, key=None, output=None, removal_expression=None, should_encrypt=True):
    """Private encrypts python files and wheel packages.
    To use the encrypted code, export the key to PRIVATE_KEY variable"""

    if removal_expression is not None and astunparse is None:
        raise ValueError("Cannot remove source code by tag without astunparse, please install it")

    if not os.path.exists(output):
        os.makedirs(output)

    if key is not None and not should_encrypt:
        raise ValueError("Cannot receive key if not encrypting code")

    if should_encrypt:
        if key is None:
            key = codecs.encode(os.urandom(KEY_SIZE), "hex")

        try:
            key = codecs.decode(key, "hex")
        except TypeError:
            raise ValueError("The key must be hexadecimal string!")
        if len(key) != KEY_SIZE:
            raise ValueError(
                "The key must be of length {}, current length is {}".format(KEY_SIZE, len(key))
            )

        logger.info("Using key {}".format(codecs.encode(key, "hex")))
        with open(os.path.join(output, "key.txt"), "w") as key_file:
            key_file.write(codecs.decode(codecs.encode(key, "hex")))

    if removal_expression is not None:
        action_list = [
            (
                lambda source: source_tags.remove_tagged_source(source, removal_expression),
                ["source"],
                "source",
            )
        ]
    else:
        action_list = []

    if should_encrypt:
        action_list.extend(
            [
                (lambda source: zlib.compress(six.b(source)), ["source"], "source"),
                (lambda source: hashlib.sha256(source).hexdigest(), ["source"], "hash"),
                (
                    lambda source: pyaes.AESModeOfOperationCTR(key).encrypt(source),
                    ["source"],
                    "source",
                ),
                (base64.b64encode, ["source"], "source"),
                (template_encrypted_code, ["source", "hash"], "source"),
            ]
        )

    result_files = []
    for path in paths:
        if not os.path.exists(path):
            logger.warning("Path {} does not exists, skipping".format(path))
            continue
        _, extension = os.path.splitext(path)
        if os.path.isdir(path):
            process_directory(path, os.path.join(output, os.path.basename(path)), action_list)
            result_files.append(os.path.join(output, path))
        elif extension == ".whl":
            process_wheel(path, output, action_list)
            result_files.append(os.path.join(output, path))
        elif extension == ".py":
            process_module(path, os.path.join(output, path), action_list)
            result_files.append(os.path.join(output, path))
        elif path.endswith(".tar.gz"):
            temp_directory = tempfile.mkdtemp()
            output_wheel, = packages.sdist_to_wheel(
                path,
                output_directory=temp_directory
            )
            process_wheel(output_wheel, output, action_list)
            result_files.append(os.path.join(output, output_wheel))
        else:
            logging.warning("Path {} must have extension .whl or .py, skipping".format(path))
    return result_files
