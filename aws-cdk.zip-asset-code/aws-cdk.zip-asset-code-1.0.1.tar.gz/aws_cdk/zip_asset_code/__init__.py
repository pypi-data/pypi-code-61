import shlex
import subprocess
import sys
import uuid
from pathlib import Path

from aws_cdk.aws_lambda import AssetCode

__all__ = ['ZipAssetCode']

# packages that are already part of the Lambda runtime which we thus do not need to package
EXCLUDE_PACKAGES = {'boto3', 'botocore', 'docutils', 'jmespath', 'pip', 'python-dateutil', 's3transfer', 'setuptools'}


def package(path_to_code: Path, working_directory=None) -> Path:
    bundle_uuid = str(uuid.uuid4()).split('-')[-1]
    target = Path('.cdk.staging') / f'asset-bundle-{bundle_uuid}'
    command = shlex.split(f'{sys.executable} -m pip install -qq --upgrade {path_to_code} --target {target.resolve()}')
    subprocess.check_call(command, cwd=working_directory)
    return target


class ZipAssetCode(AssetCode):
    """Build and package a Lambda function deployment archive with dependencies."""
    def __init__(self, path_to_code: Path, working_directory: Path = None):
        if working_directory:
            full_code_path = working_directory / path_to_code
        else:
            full_code_path = path_to_code
        if not full_code_path.is_dir():
            raise ValueError(f'{full_code_path} does not exist.')
        super().__init__(package(path_to_code, working_directory).as_posix())

    @property
    def is_inline(self) -> bool:
        return False


