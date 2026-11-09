"""Entry point for the NHL statistics application."""

from player_reader import PlayerReader
from statistics_service import StatisticsService


def main():
    """Run the NHL statistics program."""
    stats = StatisticsService(PlayerReader())
    philadelphia_flyers_players = stats.team("PHI")
    top_scorers = stats.top(10)

    print("Philadelphia Flyers:")
    for player in philadelphia_flyers_players:
        print(player)
    print()
    print("Top point getters:")
    for player in top_scorers:
        print(player)


if __name__ == "__main__":
    main()
