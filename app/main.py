import glob
from http.server import BaseHTTPRequestHandler, HTTPServer
import importlib
import os
import pkgutil
import yaml
from fastapi import FastAPI

from app import generators
from app.api import api

# Generator plugin architecture based on larose/utt
# https://mathieularose.com/plugin-architecture-in-python

def iter_namespace(ns_pkg):
    # Specifying the second argument (prefix) to iter_modules makes the
    # returned name an absolute name instead of a relative one. This allows
    # import_module to work without having to do additional modification to
    # the name.
    #
    # Source: https://packaging.python.org/guides/creating-and-discovering-plugins/
    return pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + '.')


def load_generators():
    for _, name, _ in iter_namespace(generators):
        importlib.import_module(name)


def load_config():
    config_path = os.path.join(os.getenv('CONFIG_PATH', '/config'), '*.yaml')
    config = {}
    for file in glob.glob(config_path):
        print(f'Loading config from {file}')
        try:
            config_item = yaml.safe_load(open(file))
            config[config_item['name']] = config_item['secrets']
        except yaml.YAMLError as e:
           print(f'Failed to load config file {file}: {e}')
    return config


config = load_config()
load_generators()

app = FastAPI()

@app.get('/{app_name}')
def generate_secrets(app_name: str):
  generated_secrets = {}
  for secret_request in config[app_name]:
    try:
      generated_secrets[secret_request['name']] = api.generators[secret_request['type']].generate(secret_request['parameters'])
    except KeyError:
       print(f'Generator {secret_request['type']} not found, skipping secret {secret_request['name']}')
  return generated_secrets
