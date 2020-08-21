from marshmallow import fields, ValidationError
from io import StringIO
from furl import furl
from pickle import loads,dumps
from base64 import b32encode,b32decode
from numpy import array
from requests import request
from xml.etree import ElementTree as ET
import pandas as pd
import pyotp

class FurlField(fields.Field):
    def _serialize(self, value, attr, obj, **kwargs):
        return value.url

    def _deserialize(self, value, attr, data, **kwargs):
        return furl(value)
class NumPyArrayField(fields.Field):
    def _serialize(self, value, attr, obj, **kwargs):
        return list(value)

    def _deserialize(self, value, attr, data, **kwargs):
        return array(value)
class PandasDataFrameField(fields.Field):
    def _serialize(self, value, attr, obj, **kwargs):
        return value.to_csv()

    def _deserialize(self, value, attr, data, **kwargs):
        io = StringIO(value)
        df = pd.read_csv(io)
        return df
class ElementTreeField(fields.Field):
    def _serialize(self, value, attr, obj, **kwargs):
        return (ET.tostring(value.getroot()))

    def _deserialize(self, value, attr, data, **kwargs):
        return ET.parse(value)

class HTTPRequestField(fields.Field):
    def _serialize(self, value, attr, obj, **kwargs):
        return [value.request.method,value.url]

    def _deserialize(self, value, attr, data, **kwargs):
        return request(value[0],value[1])
class ObjectField(fields.Field):
    def _serialize(self, value, attr, obj, **kwargs):
        return b32encode(dumps(value))

    def _deserialize(self, value, attr, data, **kwargs):
        return loads(b32decode(value))
class TOTPField:
    def _serialize(self, value, attr, obj, **kwargs):
        return value.secret

    def _deserialize(self, value, attr, data, **kwargs):
        return pyotp.totp.TOTP(value)
class HOTPField:
    def _serialize(self, value, attr, obj, **kwargs):
        return value.secret

    def _deserialize(self, value, attr, data, **kwargs):
        return pyotp.hotp.HOTP(value)
