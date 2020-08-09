import hashlib
import json
import yaml
import os
import sys
import shutil
from six.moves import urllib
import subprocess
import tempfile
import logging
import posixpath
import docker
import platform
from os.path import expanduser
from os.path import sep as separator
import requests
from requests.exceptions import HTTPError
import boto3
from urllib.parse import urlparse
import configparser

from mlflow.projects.backend.abstract_backend import AbstractBackend
import mlflow.tracking as tracking
from mlflow.entities import RunStatus
from mlflow.projects.submitted_run import SubmittedRun
from mlflow.projects.utils import (
    fetch_and_validate_project, get_or_create_run, load_project
)
from mlflow.utils.mlflow_tags import (
    MLFLOW_PROJECT_BACKEND
)
from infinstor_mlflow_plugin.cognito_auth_rest_store import CognitoAuthenticatedRestStore

class InfinStorSubmittedRun(SubmittedRun):
    """
    A run that just does nothing
    """

    def __init__(self, run_id):
        self._run_id = run_id

    def wait(self):
        return True

    def get_status(self):
        return RunStatus.FINISHED

    def cancel(self):
        pass

    @property
    def run_id(self):
        return self._run_id



def upload_objects(bucket_name, path_in_bucket, local_path):
    if (path_in_bucket[0] == '/'):
        path_in_bucket = path_in_bucket[1:]
    print('upload_objects: Entered. bucket=' + bucket_name + ', path_in_bucket=' + path_in_bucket\
            + ', local_path=' + local_path)
    # s3_resource = boto3.resource("s3", region_name="us-east-1")
    s3_resource = boto3.resource("s3")

    try:
        my_bucket = s3_resource.Bucket(bucket_name)

        for path, subdirs, files in os.walk(local_path):
            path = path.replace("\\","/")
            directory_name = path.replace(local_path, "")
            for onefile in files:
                src_path = os.path.join(path, onefile)
                dst_path = path_in_bucket + directory_name + '/' + onefile
                print('upload_objects: Uploading ' + src_path + ' to ' + dst_path)
                my_bucket.upload_file(src_path, dst_path)
    except Exception as err:
        print(err)

def extract_creds():
    home = expanduser("~")
    print("User's Home Directory is " + home);
    config = configparser.ConfigParser()
    credsfile = home + separator + ".aws" + separator + "credentials"
    config.read(credsfile)
    for section in config.sections():
        if (section == 'infinstor'):
            dct = dict(config[section])
            return dct['aws_access_key_id'], dct['aws_secret_access_key']
    return None, None

class PluginInfinStorProjectBackend(AbstractBackend):
    def run(self, project_uri, entry_point, params,
            version, backend_config, experiment_id, tracking_store_uri):

        print("PluginInfinStorProjectBackend: Entered. project_uri=" + str(project_uri)\
                + ", entry_point=" + str(entry_point)\
                + ", params=" + str(params)\
                + ", version=" + str(version)\
                + ", backend_config=" + str(backend_config)\
                + ", experiment_id=" + str(experiment_id)\
                + ", tracking_store_uri=" + str(tracking_store_uri))

        work_dir = fetch_and_validate_project(project_uri, version, entry_point, params)
        active_run = get_or_create_run(None, project_uri, experiment_id, work_dir, version,
                                       entry_point, params)

        print('active_run=' + str(active_run))
        print('active_run.info=' + str(active_run.info))

        artifact_uri = active_run.info.artifact_uri
        run_id = active_run.info.run_id

        tags = active_run.data.tags
        if (tags['mlflow.source.type'] != 'PROJECT'):
            raise ValueError('mlflow.source_type must be PROJECT. Instead it is '\
                    + tags['mlflow.source.type'])

        pdst = urlparse(artifact_uri)
        bucket_name = pdst.netloc
        if (pdst.path[0] == '/'):
            path_in_bucket = pdst.path[1:]
        else:
            path_in_bucket = pdst.path

        localdir = tags['mlflow.source.name']
        if ('mlflow.source.git.repoURL' in tags or
                'mlflow.gitRepoURL' in tags or
                'mlflow.source.git.commit' in tags):
            pl = urlparse(localdir)
            if (not pl.scheme == 'file'):
                raise ValueError('Cannot deal with scheme ' + pl.scheme + ' in source path')
            localdir = pl.path + separator + pl.fragment

        upload_objects(bucket_name, path_in_bucket + '/project_files', localdir)

        project = load_project(work_dir)
        tracking.MlflowClient().set_tag(active_run.info.run_id, MLFLOW_PROJECT_BACKEND, "infinstor")

        body = dict()
        body['project_files_bucket'] = bucket_name
        body['project_files_path_in_bucket'] = path_in_bucket
        body['params'] = params
        body['run_id'] = run_id
        body['experiment_id'] = str(experiment_id)
        home = expanduser("~")
        tokfile = expanduser("~") + separator + '.infinstor' + separator + '/token'
        data = open(tokfile, "r").read()
        body['dot_infinstor_contents'] = data

        key, secret = extract_creds()
        if (key != None):
            body['aws_access_key_id'] = key
            body['aws_secret_access_key'] = secret

        cog = CognitoAuthenticatedRestStore()
        headers = {
                'Content-Type': 'application/x-amz-json-1.1',
                'Authorization' : 'Bearer ' + cog.get_token_string()
                }
        url = 'https://mlflow.' + cog.get_service() + '.com/api/2.0/mlflow/projects/run-project'

        try:
            response = requests.post(url, data=json.dumps(body), headers=headers)
            response.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
            raise
        except Exception as err:
            print(f'Other error occurred: {err}')
            raise
        else:
            return InfinStorSubmittedRun(active_run.info.run_id)

