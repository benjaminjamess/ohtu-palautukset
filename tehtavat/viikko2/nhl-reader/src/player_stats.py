"""Filtering and sorting operations for NHL players."""


class PlayerStats:
    """Provide statistics queries over a collection of players."""

    def __init__(self, reader):
        """Load players from the provided reader."""
        self._players = reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        """Return players of a nationality sorted by points, descending."""
        players = [
            player
            for player in self._players
            if player.nationality == nationality
        ]
        return sorted(
            players,
            key=lambda player: player.goals + player.assists,
            reverse=True,
        )

    def top_scorers_by_team(self, team):
        """Return players on a team sorted by points, descending."""
        players = [
            player
            for player in self._players
            if player.team == team
        ]
        return sorted(
            players,
            key=lambda player: player.goals + player.assists,
            reverse=True,
        )

    def top_goal_scorers(self, how_many):
        """Palauttaa how_many eniten maaleja tehnyttä pelaajaa
        maalimäärän mukaan laskevassa järjestyksessä."""
        return sorted(
            self._players,
            key=lambda player: player.goals,
            reverse=True,
        )[:how_many]
