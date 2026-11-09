"""Read player data from the NHL statistics API."""

import requests
from player import Player


class PlayerReader:  # pylint: disable=too-few-public-methods
    """Fetch and convert player records from a configured URL."""

    def __init__(self, url):
        """Create a reader for the given player-data URL."""
        self.url = url

    def get_players(self):
        """Fetch player records and return them as Player objects."""
        response = requests.get(self.url, timeout=10)
        player_data = response.json()
        return [Player(data) for data in player_data]
