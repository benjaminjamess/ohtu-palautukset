class Player:
    def __init__(self, player_data):
        self.name = player_data["name"]
        self.nationality = player_data["nationality"]
        self.team = player_data["team"]
        self.goals = player_data["goals"]
        self.assists = player_data["assists"]

    def __str__(self):
        points = self.goals + self.assists
        return (
            f"{self.name:<22} {self.team:<4} "
            f"{self.goals} + {self.assists} = {points}"
        )
