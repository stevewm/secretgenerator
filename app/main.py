from fastapi import FastAPI, HTTPException
import importlib
import os
import pkgutil

from app import generators
import app.api as api
from app.config.file import FileConfigProvider

# Generator plugin architecture based on larose/utt
# https://mathieularose.com/plugin-architecture-in-python


def iter_namespace(ns_pkg):
    # Specifying the second argument (prefix) to iter_modules makes the
    # returned name an absolute name instead of a relative one. This allows
    # import_module to work without having to do additional modification to
    # the name.
    #
    # Source: https://packaging.python.org/guides/creating-and-discovering-plugins/
    return pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + ".")


def load_generators():
    for _, name, _ in iter_namespace(generators):
        importlib.import_module(name)


config_provider = FileConfigProvider(os.getenv("CONFIG_PATH", "/config"))
load_generators()

app = FastAPI()


@app.get("/{app_name}")
def generate_secrets(app_name: str):
    config = config_provider.get_config()  # poor man's hot reload
    if app_name not in config:
        raise HTTPException(status_code=404, detail=f"Config for {app_name} not found")

    generated_secrets = {}
    for secret_request in config[app_name]:
        secret_request["parameters"] = (
            secret_request["parameters"] if secret_request.get("parameters") else {}
        )
        try:
            generated_secrets = generated_secrets | api.get_generator(
                secret_request["type"]
            ).generate(secret_request["name"], **secret_request["parameters"])
        except KeyError:
            print(
                f"Generator {secret_request['type']} not found, \
                  skipping secret {secret_request['name']}"
            )
    return generated_secrets
