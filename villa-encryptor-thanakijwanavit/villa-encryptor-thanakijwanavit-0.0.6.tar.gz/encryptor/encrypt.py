import boto3, json

class Encryptor:
    def __init__(self, user=None , pw=None ):
        self.user = user
        self.pw = pw
    def test(self, payload = None):
        if not payload:
            payload = {
                'test': 'test'
            }
        lambda_ = boto3.client('lambda',
                       aws_access_key_id = self.user,
                       aws_secret_access_key = self.pw,
                       region_name = 'ap-southeast-1')
        response = lambda_.invoke(
          FunctionName = 'villa-wallet-dev-WalletEncryptors-C2MXDS23RI2D-test' ,
          InvocationType= 'RequestResponse',
          LogType = 'Tail',
          Payload = json.dumps(payload).encode()
        )
        return response

