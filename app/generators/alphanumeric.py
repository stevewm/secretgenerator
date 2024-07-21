import random
import string
from typing import Dict
from ..api import api


class AlphaNumeric:
    def generate(secret_name: str, length: int = 32) -> Dict[str, str]:
        return {
            secret_name: "".join(
                random.choices(string.ascii_letters + string.digits, k=length)
            )
        }


api.register_generator(AlphaNumeric)
