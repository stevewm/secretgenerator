import base64
from typing import Dict
from ..api import api


class Base64:
    def generate(secret_name, length: int = 32) -> Dict[str, str]:
        return {
            secret_name: base64.b64encode(
                api.generators["AlphaNumeric"].generate(secret_name, length)
            ).decode("utf-8")
        }


api.register_generator(Base64)
