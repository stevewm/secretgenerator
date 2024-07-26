import base64
from typing import Dict
from ..api import api


class Base64:
    def generate(secret_name, length: int = 32) -> Dict[str, str]:
        """
        Generate a random base64-encoded alphanumeric string.
        Args:
            secret_name - the name of the secret.
            length - the length of the string encoded to base64. Must be greater than 0.
        """
        return {
            secret_name: base64.b64encode(
                api.generators['AlphaNumeric']
                .generate(secret_name, length)
                .get(secret_name)
                .encode('utf-8')
            ).decode('utf-8')
        }


api.register_generator(Base64)
