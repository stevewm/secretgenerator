from typing import Generator, Type


def register_generator(generator: Type[Generator]):
    generators[generator.__name__] = generator
    print(f"Registered generator: {generator.__name__}")


def deregister_generator(generator: Type[Generator]):
    del generators[generator.__name__]
    print(f"Deregistered generator: {generator.__name__}")


def get_generator(generator_name: str) -> Type[Generator]:
    if generator_name not in generators:
        raise KeyError(f"Generator {generator_name} not found")
    return generators[generator_name]


generators = {}
