import random
import string
from typing import Dict
from ..api import api


class AlphaNumeric:
    def generate(secret_name: str, length: int = 32) -> Dict[str, str]:
        """
        Generate a random alphanumeric string.
        Args:
            secret_name - the name of the secret.
            length - the length of the string to generate. Must be greater than 0.
        """

        if length < 1:
            length = 32
        return {
            secret_name: ''.join(
                random.choices(string.ascii_letters + string.digits, k=length)
            )
        }


api.register_generator(AlphaNumeric)
