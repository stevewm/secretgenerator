import uuid
from typing import Dict
from ..api import api


class UUID:  # TODO: Support other UUID versions
    def generate(secret_name: str) -> Dict[str, str]:
        return {secret_name: str(uuid.uuid4())}


api.register_generator(UUID)
