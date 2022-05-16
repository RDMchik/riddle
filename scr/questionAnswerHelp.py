import random
import json


class QuestionHelper:
    def __init__(self, directory):
        self._dir = directory
        self.data = self.load_data()

    def load_data(self):
        with open(self._dir, 'r', encoding='utf-8') as config_file:
            data = json.load(config_file)
        return data

    def get_random(self):
        return random.choice(self.data)
