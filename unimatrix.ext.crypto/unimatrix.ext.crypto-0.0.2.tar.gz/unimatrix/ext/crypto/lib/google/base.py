"""Declares :class:`GoogleKMSInvoker`."""
from google.cloud import kms


class GoogleKMSInvoker:
    """Provides methods to invoke the Google KMS API."""

    # Maps Google algortihm version indicators to PKCS#1 OID.
    _crypto_mapping = {
        # RSA_SIGN_PKCS1_4096_SHA256
        7: "1.2.840.113549.1.1.11"
    }


    def __init__(self, project, region, keyring, key, version):
        self._google_kms = kms.KeyManagementServiceClient()
        self.__project = project
        self.__region = region
        self.__keyring = keyring
        self.__key = key
        self.__version = version

    def _get_resource_id(self):
        return self._google_kms.crypto_key_version_path(
            self.__project, self.__region, self.__keyring, self.__key,
            self.__version)
