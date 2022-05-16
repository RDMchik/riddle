from scr.configHelper import ConfigHelper
from scr.client import Client
from scr.gameManager import GameManager


config = ConfigHelper('config.json')
manager = GameManager()
client = Client(manager, config)

client.run(config.data["token"])
