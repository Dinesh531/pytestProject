import os
from configparser import ConfigParser

config = ConfigParser()
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config_path = os.path.join(base_dir, "config", "config.ini")
config.read(config_path)

class ReadConfig:

    @staticmethod
    def get_base_url():
        return config.get("common info", "baseURL")

    @staticmethod
    def get_api_url():
        return config.get("common info", "apiURL")

    @staticmethod
    def get_browser():
        return config.get("common info", "browser")