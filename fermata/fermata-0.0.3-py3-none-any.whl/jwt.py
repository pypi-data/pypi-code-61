import hmac
import hashlib
import json
import time
from base64 import urlsafe_b64decode
from base64 import urlsafe_b64encode


def hs256(key: bytes, content: bytes):
    sign = hmac.new(key, content, hashlib.sha256).digest()
    return b64encode(sign)


SUPPORT_ALGORITHMS = {
    'HS256': hs256
}
DEFAULT_ALGORITHMS = 'HS256'
TOKEN_TTL = 8 * 60 * 60


class ExpiredToken(ValueError):
    pass


class InvalidToken(ValueError):
    pass


def b64encode(s: bytes):
    return urlsafe_b64encode(s).rstrip(b'=')


def b64decode(s: str):
    return urlsafe_b64decode(s + '=' * (len(s) % 4))


def loads(key: str, token: str, check_exp=True):
    terms = token.strip().split('.')
    alg = DEFAULT_ALGORITHMS
    if len(terms) < 3:
        raise InvalidToken(f'invalid token `{token}`')
    header, payload, signature = terms[-3:]
    # select alg by header
    if header:
        # raise ValueError
        h = json.loads(b64decode(header))
        try:
            alg = h.get('alg', DEFAULT_ALGORITHMS)
        except AttributeError:
            raise InvalidToken(f'bad header `{token}`')

        if alg not in SUPPORT_ALGORITHMS:
            raise InvalidToken(f'unsupported alg `{token}`')

    sign = SUPPORT_ALGORITHMS[alg]

    content = (header + '.' + payload).encode('u8')
    if signature.encode('u8') != sign(key.encode('u8'), content):
        raise InvalidToken(f'invalid signature `{token}`')

    # raise ValueError
    payload = json.loads(b64decode(payload))

    # exp check
    if check_exp and int(payload.get('exp', 0)) < time.time():
        raise ExpiredToken(f'expired token `{token}`')

    return payload


def dumps(key: str, payload: dict, dump_header=False):
    header = {'alg': 'HS256', 'typ': 'JWT'}
    header, payload = [b64encode(
                json.dumps(
                    v,
                    ensure_ascii=False,
                    separators=(',', ':')
                ).encode('u8')
            )
            for v in (header, payload)]
    if not dump_header:
        header = b''
    content = header + b'.' + payload
    sign = hs256(key.encode('u8'), content)
    token = content + b'.' + sign
    return token.decode()


def build(
        key,
        user_id,
        refresh_token,
        scopes=None,
        data=None,
        ttl=TOKEN_TTL,
    ):
    payload = {
        'sub': user_id,
        'exp': int(time.time()) + ttl
    }
    if data:
        payload['data'] = data
    if scopes:
        payload['scopes'] = scopes
    return {
        'access_token': dumps(key, payload),
        'token_type': 'Bearer',
        'expires_in': ttl,
        'refresh_token': refresh_token,
    }


class JWT:

    def __init__(self, key):
        self.key = key

    def loads(self, token, check_exp=True):
        return loads(self.key, token, check_exp)

    def dumps(self, payload, dump_header=False):
        return dumps(self.key, payload, dump_header)

    def build(
        self,
        user_id,
        refresh_token,
        scopes=None,
        data=None,
        ttl=TOKEN_TTL,
    ):
        return build(self.key, user_id, refresh_token, scopes, data, ttl)

