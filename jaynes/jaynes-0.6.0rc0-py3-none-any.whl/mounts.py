import os
from uuid import uuid4

from .helpers import get_temp_dir
from os.path import join as pathJoin


class Simple:
    """Mount a directory from the remote host to docker

    :param host_path: path on the host
    :param container_path: path inside the container
    :param pypath: boolean flag for whether this mount point should be included in the PYPATH environment variable
    """

    def __init__(self, host_path, container_path, pypath=False):
        # host_path = remote if os.path.isabs(remote) else pathJoin(self.remote_cwd, remote)
        assert os.path.isabs(host_path), "remote path has to be absolute"
        assert os.path.isabs(container_path), "docker linked path has to be absolute"
        self.docker_mount = f"-v '{host_path}':'{container_path}'"
        self.host_path = host_path
        self.container_path = container_path
        self.pypath = pypath


class S3Code:
    """
    Tars a local folder, uploads the content to S3, downloads the tar ball on the remote instance and mounts it
    in docker.

    To configure in the yaml file, you can do:

    .. code:: yaml

        mounts: # mount configurations Available keys: NOW, UUID,
        - !mounts.S3Code &code_mount
          s3_prefix: s3://ge-bair/jaynes-debug
          local_path: .
          host_path: /home/ubuntu/jaynes-mounts/{now:%Y-%m-%d}/{now:%H%M%S.%f}
          # container_path: /Users/geyang/learning-to-learn
          pypath: true
          excludes: "--exclude='*__pycache__' --exclude='*.git' --exclude='*.idea' --exclude='*.egg-info' --exclude='*.pkl'"
          compress: true
        - !mounts.S3Code &fair_code_mount
          s3_prefix: s3://ge-bair/jaynes-debug
          local_path: .
          host_path: /private/home/geyang/jaynes-mounts/{now:%Y-%m-%d}/{now:%H%M%S.%f}
          pypath: true
          excludes: "--exclude='*__pycache__' --exclude='*.git' --exclude='*.idea' --exclude='*.egg-info' --exclude='*.pkl'"
          compress: true


    :param local_path: path to the local directory. Doesn't have to be absolute.
    :param s3_prefix: The s3 prefix including the s3: protocol, the bucket, and the path prefix.
    :param host_path: The path on the remote instance. Default /tmp/{uuid4()}
    :param name: the name for the tar ball. Default to {uuid4()}
    :param container_path: The path for the docker instance. Can be something like /Users/ge/project-folder/blah
    :param pypath (bool): Whether this directory should be added to the python path
    :param excludes: The files paths to exclude, default to "--exclude='*__pycache__'"
    :param file_mask: The file mask for files to include. Default to "."
    :return: self
    """

    def __init__(self, *, s3_prefix, local_path, host_path=None, remote_tar=None, container_path=None, pypath=False,
                 excludes=None, file_mask=None, name=None, compress=True, public=True, no_signin=True):
        # I fucking hate the behavior of python defaults. -- GY
        file_mask = file_mask or "."  # file_mask can Not be None or "".
        excludes = excludes or "--exclude='*__pycache__' --exclude='*.git' --exclude='*.idea' --exclude='*.egg-info'"
        name = name or uuid4()
        tar_name = f"{name}.tar"
        self.temp_dir = get_temp_dir()
        local_tar = pathJoin(self.temp_dir, tar_name)
        from .jaynes import RUN
        local_abs = os.path.join(RUN.project_root, local_path)
        if host_path:
            assert os.path.isabs(host_path), "host_path path has to be absolute"
        else:
            host_path = f"/tmp/{name}"

        from .jaynes import RUN
        docker_abs = os.path.join(RUN.project_root, container_path) if container_path else local_abs
        self.local_script = f"""
                type gtar >/dev/null 2>&1 && alias tar=`which gtar`
                mkdir -p '{self.temp_dir}'
                # Do not use absolute path in tar.
                tar {excludes} -c{"z" if compress else ""}f '{local_tar}' -C '{local_abs}' {file_mask}
                # aws s3 cp '{local_tar}' '{s3_prefix}/{tar_name}' --only-show-errors
                aws s3 cp '{local_tar}' '{s3_prefix}/{tar_name}' {'--acl public-read-write' if public else ''}
                """
        remote_tar = remote_tar or f"/tmp/{tar_name}"
        self.host_path = host_path
        self.host_setup = f"""
                aws s3 cp '{pathJoin(s3_prefix, tar_name)}' '{remote_tar}' {'--no-sign-request' if no_signin else ''}
                mkdir -p '{host_path}'
                tar -{"z" if compress else ""}xf '{remote_tar}' -C '{host_path}'
                """
        self.pypath = pypath
        self.container_path = docker_abs
        self.docker_mount = f"-v '{host_path}':'{docker_abs}'"


class S3Output:
    """
    Mounting a remote directory to docker, and upload it's content periodically to s3.

    **To Avoid downloading to local during startup**: set local to None

    s3 path syntax:
                {s3_prefix}{s3_dir}
    local path syntax:
                file://{local}
    remote path syntax:
                ssh://<remote>:{remote if isabs(remote) else remote_cwd + remote}
            note that the remote path is made absolute using the remote_cwd parameter

    :param name:
    :param s3_prefix: Need slash at the end.
    :param local_path: When None, do not download those files
    :param interval:
    :param pypath:
    :param sync_s3:
    :return:
    """

    def __init__(self, *, container_path, s3_prefix, host_path=None, name=None, local_path=None, interval=15,
                 pypath=False, sync_s3=True):

        if host_path is None:
            host_path = f"/tmp/jaynes_mounts/{uuid4() if name is None else name}"
        else:
            assert os.path.isabs(host_path), "ATTENTION: host_path path has to be an absolute path."

        # used for getting the container log path
        self.host_path = host_path

        assert os.path.isabs(container_path), \
            "ATTENTION: docker path has to be absolute, to make sure your code knows where it is writing to."
        if local_path:
            download_script = f"""
                aws s3 cp --recursive {s3_prefix} '{local_path}' || echo "s3 bucket is EMPTY" """
            self.local_script = f"""
                mkdir -p '{local_path}'
                while true; do
                    echo "downloading..." {download_script}
                    {f"sleep {interval}" if interval else ""}
                done & echo 'sync {local_path} initiated'
            """
        else:
            print('S3UploadMount(**{}) generated no local_script.'.format(locals()))
            # pass
        self.upload_script = f"""
                aws s3 cp --recursive '{host_path}' {s3_prefix} """  # --only-show-errors"""
        self.host_setup = f"""
                echo 'making main_log directory {host_path}'
                mkdir -p '{host_path}'
                echo "made main_log directory" """ + ("" if not sync_s3 else f"""
                while true; do
                    echo "uploading..." {self.upload_script}
                    {f"sleep {interval}" if interval else ""}
                done & echo "sync {host_path} initiated" 
                while true; do
                    if [ -z $(curl -Is http://169.254.169.254/latest/meta-data/spot/termination-time | head -1 | grep 404 | cut -d \  -f 2) ]
                    then
                        logger "Running shutdown hook." {self.upload_script}
                        break
                    else
                        # Spot instance not yet marked for termination. This is hoping that there's at least 3 seconds
                        # between when the spot instance gets marked for termination and when it actually terminates.
                        sleep 3
                    fi
                done & echo main_log sync initiated
                """)
        self.docker_mount = f"-v '{host_path}':'{container_path}'"
        self.container_path = container_path
        self.pypath = pypath


# New
class SSHCode:
    """
    Tars a local folder, uploads the content to S3, downloads the tar ball on the remote instance and mounts it
    in docker.


    :param profile: The profile to use for untaring the code ball. Not used.
    :param password: The password to use for untaring the code ball. Not used.
    :param local_path: path to the local directory. Doesn't have to be absolute.
    :param s3_prefix: The s3 prefix including the s3: protocol, the bucket, and the path prefix.
    :param host_path: The path on the remote instance. Default /tmp/{uuid4()}
    :param name: the name for the tar ball. Default to {uuid4()}
    :param container_path: The path for the docker instance. Can be something like /Users/ge/project-folder/blah
    :param pypath (bool): Whether this directory should be added to the python path
    :param excludes: The files paths to exclude, default to "--exclude='*__pycache__'"
    :param file_mask: The file mask for files to include. Default to "."
    :return: self
    """

    def __init__(self, *, username, ip, pem=None, port=None, profile=None, password=None, local_path=None,
                 host_path=None, remote_tar=None,
                 container_path=None, pypath=False, excludes=None, file_mask=None, name=None, compress=True):
        # I fucking hate the behavior of python defaults. -- GY
        file_mask = file_mask or "."  # file_mask can Not be None or "".
        excludes = excludes or "--exclude='*__pycache__' --exclude='*.git' --exclude='*.idea' --exclude='*.egg-info'"
        name = name or uuid4()
        tar_name = f"{name}.tar"
        self.temp_dir = get_temp_dir()
        local_tar = pathJoin(self.temp_dir, tar_name)
        from .jaynes import RUN
        local_abs = os.path.join(RUN.project_root, local_path)
        if host_path:
            assert os.path.isabs(host_path), "host_path path has to be absolute"
        else:
            host_path = f"/tmp/{name}"

        from .jaynes import RUN
        docker_abs = os.path.join(RUN.project_root, container_path) if container_path else local_abs
        remote_tar = remote_tar or f"/tmp/{tar_name}"

        port_ = "" if port is None else f"-p {port}"
        pem_ = "" if pem is None else f"-i {pem}"

        # scp does not allow file rename.
        remote_tar_dir = os.path.dirname(remote_tar)
        scp_script = f"scp {port_.upper()} {pem} {local_tar} {username}@{ip}:{remote_tar_dir}"
        ssh_string = f"'ssh {port_} {pem_}'" if port_ or pem_ else 'ssh'
        rsync_script = f"rsync -az -e {ssh_string} {local_tar} {username}@{ip}:{remote_tar}"
        if password is not None:  # note: now supports password log in!
            # rsync_script = f'expect <<EOF\nspawn {rsync_script};expect \"password:\";send \"{password}\\r\"\nEOF'
            # need to install sshpass from:
            # https://gist.github.com/arunoda/7790979
            rsync_script = f"sshpass -p '{password}' {rsync_script}"

        self.local_script = f"""
                type gtar >/dev/null 2>&1 && alias tar=`which gtar`
                mkdir -p '{self.temp_dir}'
                # Do not use absolute path in tar.
                tar {excludes} -c{"z" if compress else ""}f '{local_tar}' -C '{local_abs}' {file_mask}
                {rsync_script}
                """
        self.host_path = host_path
        self.host_setup = f"""
                mkdir -p '{host_path}'
                tar -{"z" if compress else ""}xf '{remote_tar}' -C '{host_path}'
                """
        self.pypath = pypath
        self.container_path = docker_abs
        self.docker_mount = f"-v '{host_path}':'{docker_abs}'"
