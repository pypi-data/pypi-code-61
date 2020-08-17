"""Python modules and distribution encryption tool"""
import base64
import hashlib
import logging
import os
import re
import zipfile
import zlib

import click
try:
    import wheelmerge
except ImportError:
    wheelmerge = None

from . import processor
from . import loader
from .loader import load_module_content


logging.basicConfig(format="%(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)


def tag(*names):
    return lambda function: function


@click.command()
@click.argument("paths", nargs=-1, type=click.Path())
@click.option("-k", "--key", type=str, default=None)
@click.option("-o", "--output", type=click.Path(), default="output")
@click.option("-p", "--predicate", "removal_expression", type=str, default=None)
@click.option("--encrypt/--no-encrypt", " /-n", default=True)
@click.option("--zip/--no-zip", "-z/ ", "should_zip", default=False)
def private(paths, key, output, removal_expression, encrypt, should_zip):
    try:
        output_wheels = processor.process_paths(
            paths,
            key=key,
            output=output,
            removal_expression=removal_expression,
            should_encrypt=encrypt
        )
        if should_zip:
            wheelmerge.merge_wheels(
                output_wheels,
                os.path.join(output, "packed.zip"),
                additional_files={
                    loader.__file__.replace(".pyc", ".py"): "private.py"
                }
            )
    except ValueError as exception:
        logger.exception("Failed with error:")
        exit(1)


def main():
    private()


if __name__ == "__main__":
    main()
