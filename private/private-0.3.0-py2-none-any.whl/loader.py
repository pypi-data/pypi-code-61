import base64
import hashlib
import os
import zlib

import pyaes


def load_module_content(encrypted_module, key, code_hash):
    """Decrypt encrypted code and validates against hash.
    It should only be used internally by encrypted modules."""
    decryptor = pyaes.AESModeOfOperationCTR(key)
    decrypted_module = decryptor.decrypt(
        base64.b64decode(encrypted_module.strip().replace(os.linesep, ""))
    )
    if hashlib.sha256(decrypted_module).hexdigest() != code_hash:
        raise ValueError("Decrypted code hash mismatch! Key may be wrong")
    decrypted_module = zlib.decompress(decrypted_module)
    return decrypted_module


