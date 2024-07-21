import random
import string
from typing import Any, Dict
from ..api import api

class AlphaNumeric():
    def generate(parameters: Dict[str, Any]) -> str:
        return ''.join(random.choices(string.ascii_letters + string.digits, k=parameters.get('length', 32)))


api.register_generator(AlphaNumeric)
