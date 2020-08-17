import glob
import logging
import os
import re

import pip


logger = logging.getLogger(__name__)
PACKAGE_NAME = re.compile("(.+\d+\.\d+(?:\.\d+)?)")


def sdist_to_wheel(*file_paths, **kwargs):
    logger.info("Converting sdists to wheels: {}".format(", ".join(file_paths)))
    output_directory = kwargs.pop("output_directory", ".")

    wheel_command = pip.commands_dict["wheel"]()
    options, _ = wheel_command.cmd_opts.parser.parse_args([])
    options.ignore_dependencies = True
    options.wheel_dir = output_directory

    # Disable all output
    old_level = pip.logger.level
    pip.logger.setLevel(logging.CRITICAL)
    try:
        wheel_command.run(options, list(file_paths))
    finally:
        pip.logger.setLevel(old_level)

    result = [
        glob.glob(
            os.path.join(
                output_directory,
                PACKAGE_NAME.match(file_name).groups()[0] + "*.whl")
        )
        for file_name in file_paths
    ]
    if not all(len(glob_list) == 1 for glob_list in result):
        raise ValueError("Invalid number of output files: {}".format(result))
    else:
        return [glob_list[0] for glob_list in result]
