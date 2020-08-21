from furl import furl
from flask import request

PROTO_HEADER = "X-Forwarded-Proto"

def get_url():
    new_scheme = request.headers.get(PROTO_HEADER, request.scheme)
    return furl(request.url).set(scheme = new_scheme)