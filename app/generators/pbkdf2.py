import hashlib
from typing import Dict
from ..api import api


class PBKDF2:
    def generate(
        secret_name,
        length: int = 32,
        hash_name: str = "sha512",
        digest_name: str = None,
        rounds: int = 310000,
        salt_length: int = 16,
    ) -> Dict[str, str]:
        if digest_name is None:
            digest_name = f"{secret_name}_digest"

        secret_string = api.get_generator("AlphaNumeric").generate(secret_name, length)[
            secret_name
        ]
        salt = api.get_generator("AlphaNumeric").generate("salt", salt_length)["salt"]
        print(secret_string)
        print(salt)
        secret_hash = hashlib.pbkdf2_hmac(
            hash_name, bytes(secret_string, "utf-8"), bytes(salt, "utf-8"), rounds
        ).hex()

        return {secret_name: secret_string, digest_name: secret_hash}


api.register_generator(PBKDF2)
