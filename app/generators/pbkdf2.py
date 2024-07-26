import binascii
import hashlib
from typing import Dict
from ..api import api


class PBKDF2:
    def generate(
        secret_name,
        digest_name: str = None,
        length: int = 32,
        hash_name: str = 'sha512',
        rounds: int = 310000,
        salt_length: int = 16,
    ) -> Dict[str, str]:
        """
        Generate a random PBKDF2 hash digest.
        Returns a dictionary containing the secret and digest.
        Args:
            secret_name - the name of the secret.
            digest_name - the name of the digest. Default: {secret_name}_digest.
            length - the length of the string encoded to base64. Must be greater than 0.
            hash_name - the name of the hash algorithm to use. Default: 'sha512'.
            rounds - the number of iterations to use. Default: 310000.
            salt_length - the length of the salt to generate. Default: 16.
        """
        if digest_name is None:
            digest_name = f'{secret_name}_digest'

        # Generate secret and salt
        secret_string = (
            api.get_generator('AlphaNumeric')
            .generate(secret_name, length)
            .get(secret_name)
            .encode('utf-8')
        )
        salt = (
            api.get_generator('AlphaNumeric')
            .generate('salt', salt_length)
            .get('salt')
            .encode('utf-8')
        )

        # Hash secret
        secret_hash = hashlib.pbkdf2_hmac(hash_name, secret_string, salt, rounds)

        salt_hex = binascii.hexlify(salt).decode('utf-8')
        password_hash = binascii.hexlify(secret_hash).decode('utf-8')

        # $pbkdf2$iterations$saltinhexstring$hash64bytesinhexstring
        secret_hash = f'$pbkdf2-${hash_name}${rounds}${salt_hex}${password_hash}'

        return {secret_name: secret_string, digest_name: secret_hash}


api.register_generator(PBKDF2)
