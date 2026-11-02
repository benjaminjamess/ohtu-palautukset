import unittest
from statistics_service import StatisticsService, SortBy
from player import Player


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri", "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]


class TestStatisticsService(unittest.TestCase):

    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search_finds_player(self):
        player = self.stats.search("Semenko")
        self.assertEqual(player.name, "Semenko")

    def test_search_does_not_find_player(self):
        player = self.stats.search("Unknown")
        self.assertIsNone(player)

    def test_team_returns_players_from_team(self):
        players = self.stats.team("EDM")
        names = [player.name for player in players]

        self.assertEqual(names, ["Semenko", "Kurri", "Gretzky"])

    def test_team_returns_empty_list_for_unknown_team(self):
        players = self.stats.team("UNKNOWN")
        self.assertEqual(players, [])

    def test_top_returns_players_in_points_order(self):
        players = self.stats.top(3)
        names = [player.name for player in players]

        self.assertEqual(names, ["Gretzky", "Lemieux", "Yzerman"])

    def test_top_by_points(self):
        players = self.stats.top(3, SortBy.POINTS)
        names = [player.name for player in players]

        self.assertEqual(names, ["Gretzky", "Lemieux", "Yzerman"])

    def test_top_by_goals(self):
        players = self.stats.top(3, SortBy.GOALS)
        names = [player.name for player in players]

        self.assertEqual(names, ["Lemieux", "Yzerman", "Kurri"])

    def test_top_by_assists(self):
        players = self.stats.top(3, SortBy.ASSISTS)
        names = [player.name for player in players]

        self.assertEqual(names, ["Gretzky", "Yzerman", "Lemieux"])

    def test_top_defaults_to_points(self):
        players = self.stats.top(3)
        names = [player.name for player in players]

        self.assertEqual(names, ["Gretzky", "Lemieux", "Yzerman"])


if __name__ == "__main__":
    unittest.main()