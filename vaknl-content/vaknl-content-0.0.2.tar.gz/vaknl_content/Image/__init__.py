__author__ = "Wytze Bruinsma"

import os
from dataclasses import dataclass, field
from io import BytesIO

import requests
from PIL import Image
from vaknl_gcp.Storage import StorageClient

from vaknl_content import Content


@dataclass
class Image(Content):
    url: str = None  # original url
    bucket_url: str = None  # bucket url
    width: int = None  # pixel with
    height: int = None  # pixel height
    bytes_size: int = None  # bytes size of image
    sort_index: str = None


class ImageClient(object):

    def __init__(self, project_id):
        self.project_id = project_id
        self.storage_client = StorageClient(project=project_id)

    @staticmethod
    def get_image(image_url, auth=None, headers=None):
        for i in range(3):  # try 3 times if necessary
            try:
                response = requests.get(image_url, headers=headers, auth=auth)
                if response.status_code <= 204:
                    data = response.content
                    with Image.open(BytesIO(data)).convert('RGB') as img:
                        # convert to webp
                        with BytesIO() as bytes:
                            img.save(bytes, format='webp')
                            with Image.open(bytes) as web_img:
                                file_name = ''.join(os.path.basename(image_url).split('.')[0]) + '.webp'
                                width, height = web_img.size
                                size = web_img.tell()
                                return file_name, width, height, size, data
            except Exception as e:
                print(e)
        return None, None, None, None, None

    def upload_image_to_storage(self, id, bucket_name, image_url, auth=None):
        file_name, width, heigth, byte_size, image = self.get_image(image_url, auth)
        if image:
            bucket = self.storage_client.get_bucket(f'{bucket_name}-{self.project_id}')
            blob = bucket.blob(f"{id}/{file_name}")
            new_image_url = blob.upload_from_string(image)
            return width, heigth, byte_size, new_image_url
        else:
            return None, None, None, None
