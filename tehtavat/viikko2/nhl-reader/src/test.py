"""Print the Dallas Stars players sorted by points."""

from player_reader import PlayerReader
from player_stats import PlayerStats

PLAYER_URL = "https://studies.cs.helsinki.fi/nhlstats/2026-27/players"
stats = PlayerStats(PlayerReader(PLAYER_URL))

for p in stats.top_scorers_by_team("DAL"):
    print(p)
