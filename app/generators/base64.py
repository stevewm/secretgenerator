import base64
from typing import Any, Dict
from ..api import api

class Base64():
    def generate(parameters: Dict[str, Any]) -> str:
        return base64.b64encode(api.generators['AlphaNumeric'].generate({'length': parameters.get('length', 32)})).decode('utf-8')


api.register_generator(Base64)
