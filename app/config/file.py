import glob
import os
import yaml


class FileConfigProvider:
    def __init__(self, config_path):
        self.__config_path = config_path

    def get_config(self):
        config_files = os.path.join(self.__config_path, '*.yaml')
        config = {}
        for file in glob.glob(config_files):
            print(f'Loading config from {file}')
            try:
                config_item = yaml.safe_load(open(file))
                if config_item['name']:
                    config[config_item['name']] = config_item['secrets']
                else:
                    print(f'Config file {file} has no name attribute, skipping')
            except yaml.YAMLError as e:
                print(f'Failed to load config file {file}: {e}')
        print(config)
        return config
