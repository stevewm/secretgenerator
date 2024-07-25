import glob
import os
import yaml


class FileConfigProvider:
    def __init__(self, config_path):
        self.__config_path = config_path

    def get_config(self):
        config_files = os.path.join(self.__config_path, "*.yaml")
        config = {}
        for file in glob.glob(config_files):
            print(f"Loading config from {file}")
            print(file)
            try:
                config_item = yaml.safe_load(open(file))
                config[config_item["name"]] = config_item["secrets"]
            except yaml.YAMLError as e:
                print(f"Failed to load config file {file}: {e}")
        return config
