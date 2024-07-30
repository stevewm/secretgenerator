from passlib.hash import pbkdf2_sha512
from typing import Dict
from ..api import api


class PBKDF2:
    def generate(
        secret_name,
        digest_name: str = None,
        length: int = 32,
        iterations: int = 310000,
        salt_length: int = 16,
    ) -> Dict[str, str]:
        """
        Generate a random SHA-512 PBKDF2 hash digest.
        Returns a dictionary containing the secret and digest.
        Args:
            secret_name - the name of the secret.
            digest_name - the name of the digest. Default: {secret_name}_digest.
            length - the length of the random password string. Must be greater than 0.
            iterations - the number of iterations to use. Default: 310000.
            salt_length - the length of the salt to generate. Default: 16.
        """
        if digest_name is None:
            digest_name = f'{secret_name}_digest'

        secret_string = (
            api.get_generator('AlphaNumeric')
            .generate(secret_name, length)
            .get(secret_name)
            .encode()
        )
        salt = (
            api.get_generator('AlphaNumeric')
            .generate('salt', salt_length)
            .get('salt')
            .encode()
        )

        secret_hash = pbkdf2_sha512.using(iterations=iterations, salt=salt).hash(
            secret_string
        )
        return {secret_name: secret_string, digest_name: secret_hash}


api.register_generator(PBKDF2)
