import boto3


class Encryptor:
    def __init__(self, user=None , pw=None ):
        self.user = user
        self.pw = pw

