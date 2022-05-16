import json


class ConfigHelper:
    def __init__(self, config_directory):
        self._dir = config_directory
        self.data = self.load_config_data()

    def load_config_data(self):
        with open(self._dir, 'r') as config_file:
            data = json.load(config_file)
        return data
