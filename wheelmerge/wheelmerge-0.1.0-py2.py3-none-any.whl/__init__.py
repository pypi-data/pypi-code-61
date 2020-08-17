import os
import sys
import zipfile

import entrypoints


MAIN_FILE_NAME = '__main__.py'
MAIN_FILE_PATH = os.path.join(os.path.dirname(__file__), MAIN_FILE_NAME)
ENTRYPOINTS_MODULE_PATH = entrypoints.__file__.replace(".pyc", ".py")


def merge_zip_files(zip_files_to_merge, output_path, files_to_add={}):
    with zipfile.ZipFile(output_path, "a") as output_file:
        for zip_path in zip_files_to_merge:
            with zipfile.ZipFile(zip_path, "r") as zip_file:
                for zip_entry in zip_file.namelist():
                    output_file.writestr(zip_entry, zip_file.open(zip_entry).read())
        for source_path, dest_path in files_to_add.items():
            with open(source_path, "r") as source_file:
                output_file.writestr(dest_path, source_file.read())


def merge_wheels(wheels_to_merge, output_path, additional_files={}):
    additional_files.update({
        MAIN_FILE_PATH: MAIN_FILE_NAME,
        ENTRYPOINTS_MODULE_PATH: os.path.basename(ENTRYPOINTS_MODULE_PATH)
    })
    merge_zip_files(wheels_to_merge, output_path, files_to_add=additional_files)


def main():
    zip_files_to_merge = sys.argv[1:-1]
    output_path = sys.argv[-1]
    merge_wheels(zip_files_to_merge, output_path)


if __name__ == '__main__':
    main()
