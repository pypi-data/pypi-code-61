import os
import requests
import json
from urllib3 import disable_warnings
from urllib3.exceptions import InsecureRequestWarning
from pycrypt.encryption import Encryption, AESCipher
from pyucs.log.decorators import addClassLogger


@addClassLogger
class Credential:

    def __init__(self, username):
        self.username = username
        self.session = requests.Session()
        self.session.verify = False
        disable_warnings(InsecureRequestWarning)
        self.__password = None
        self.__private_file = os.environ.get('RSAPrivateFile' or None)
        self.__secret = open(os.environ.get('RSASecret' or None), 'r').read().strip()

    def get_credential(self, dev=False):
        try:
            if dev:
                credstore_uri = 'https://credstore-dev/credentialstore/GetCredential?ClientId={}&username={}'.format(
                    os.environ['ClientId'],
                    self.username
                )
            else:
                credstore_uri = 'https://credstore/credentialstore/GetCredential?ClientId={}&username={}'.format(
                    os.environ['ClientId'],
                    self.username
                )
            self.__log.info(f"API call to {credstore_uri}")
            response = self.session.get(url=credstore_uri)
            data = json.loads(response.text)
            self.__log.debug(f"API response JSON: {data}")

            self.decipher(
                shared_key=data[0].get('secret' or None)[0].get('shared_key' or None),
                password=data[0].get('secret' or None)[0].get('password' or None)
            )

            return {
                'username': self.username,
                'password': self.__password
            }
        except BaseException as e:
            self.__log.exception(f'Exception: {e}, \n Args: {e.args}')

    def decipher(self, shared_key, password):
        try:
            aes_cipher = AESCipher()
            rsa_cipher = Encryption()
            self.__log.debug(f"RSA Cipher decrypting {shared_key}")
            rsa_cipher.decrypt(encrypted_data=shared_key, private_key_file=self.__private_file, secret_code=self.__secret)
            self.__log.debug(f"AES Cipher decrypting {password}")
            self.__password = aes_cipher.decrypt(enc=password, key=rsa_cipher.get_decrypted_message())
            self.__secret = None
        except BaseException as e:
            self.__log.error(f"Credstore Decipher error: {e}")
            self.__log.exception(f'Exception: {e}, \n Args: {e.args}')
