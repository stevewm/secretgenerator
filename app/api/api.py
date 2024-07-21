from typing import Generator, Type

def register_generator(generator: Type[Generator]):
    generators[generator.__name__] = generator
    print(f"Registered generator: {generator.__name__}")

def deregister_generator(generator: Type[Generator]):
    del generators[generator.__name__]
    print(f"Deregistered generator: {generator.__name__}")

generators = {}
