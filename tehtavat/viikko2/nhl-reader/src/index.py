"""Command-line application for querying NHL player statistics."""

from rich.console import Console
from rich.table import Table

from player_reader import PlayerReader
from player_stats import PlayerStats


def display_players(title, players):
    """Display players and their scoring statistics in a table."""
    table = Table(title=title)
    table.add_column("Player")
    table.add_column("Team")
    table.add_column("Goals", justify="right")
    table.add_column("Assists", justify="right")
    table.add_column("Points", justify="right", style="bold")

    for player in players:
        points = player.goals + player.assists
        table.add_row(
            player.name,
            player.team,
            str(player.goals),
            str(player.assists),
            str(points),
        )

    Console().print(table)


def main():
    """Prompt for a nationality, team, and season, then display results."""
    nationality = input("Nationality code: ")
    team = input("Team code: ")
    season = input("Season (e.g. 2024-25): ")

    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    nationality_players = stats.top_scorers_by_nationality(nationality)
    team_players = stats.top_scorers_by_team(team)

    display_players(f"Players from {nationality} ({season})", nationality_players)
    display_players(f"Players from {team} ({season})", team_players)


if __name__ == "__main__":
    main()
