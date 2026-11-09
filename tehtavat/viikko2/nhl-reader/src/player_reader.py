import requests

from player import Player


class PlayerReader:
    def __init__(self, url):
        self.url = url

    def get_players(self):
        response = requests.get(self.url)
        player_data = response.json()
        return [Player(data) for data in player_data]