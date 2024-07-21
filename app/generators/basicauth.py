from typing import Any, Dict
from ..api import api

class BasicAuth():
    def generate(parameters: Dict[str, Any]) -> str:
        username = parameters.get('username', 'admin')
        password = api.generators['AlphaNumeric'].generate({'length': parameters.get('length', 32)})
        return f'{username}:{password}'


api.register_generator(BasicAuth)
