import base64
from .base64 import Base64


def test_length():
    secret = Base64.generate('secret', 10).get('secret')
    decoded_secret = base64.b64decode(secret)
    assert len(decoded_secret) == 10


def test_negative_length():
    secret = Base64.generate('secret', -1).get('secret')
    decoded_secret = base64.b64decode(secret)
    assert len(decoded_secret) == 32
