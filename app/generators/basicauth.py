from typing import Dict
from ..api import api


class BasicAuth:
    def generate(
        secret_name, username: str = 'admin', length: int = 32
    ) -> Dict[str, str]:
        """
        Generate a basic auth string in the format of username:password.
        Args:
            secret_name - the name of the secret.
            username - the username in the basic auth string. Default: 'admin'.
            length - the length of the password. Must be greater than 0.
        """
        password = api.generators['AlphaNumeric'].generate('password', length)[
            'password'
        ]
        return {secret_name: f'{username}:{password}'}


api.register_generator(BasicAuth)
