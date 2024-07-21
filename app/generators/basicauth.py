from typing import Dict
from ..api import api


class BasicAuth:
    def generate(
        secret_name, username: str = "admin", length: int = 32
    ) -> Dict[str, str]:
        password = api.generators["AlphaNumeric"].generate(username, length)[username]
        return {secret_name: f"{username}:{password}"}


api.register_generator(BasicAuth)
