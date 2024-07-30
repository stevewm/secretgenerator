import binascii
from typing import Dict
from ..api import api
import bcrypt


class BCrypt:
    def generate(
        secret_name,
        length: int = 32,
        digest_name: str = None,
    ) -> Dict[str, str]:
        """
        Generate a bcrypt password hash digest. Intended for use with glauth.
        Args:
            secret_name - the name of the secret.
            length - the length of the password. Must be greater than 0.
        """
        if digest_name is None:
            digest_name = f'{secret_name}_digest'

        password = (
            api.generators['AlphaNumeric'].generate('secret', length).get('secret')
        )
        hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        return {secret_name: password, digest_name: binascii.hexlify(hash)}


api.register_generator(BCrypt)
