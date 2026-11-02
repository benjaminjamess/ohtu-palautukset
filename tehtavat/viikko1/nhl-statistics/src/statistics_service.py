from player_reader import PlayerReader
from enum import Enum

class SortBy(Enum):
    POINTS=1
    GOALS=2
    ASSISTS=3



class StatisticsService:
    def __init__(self,player_reader):
        self._players = player_reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)

    def top(self, how_many, sort_by=SortBy.POINTS):
        def sort_by_points(player):
            return player.points

        def sort_by_goals(player):
            return player.goals

        def sort_by_assists(player):
            return player.assists

        if sort_by == SortBy.POINTS:
            key = sort_by_points
        elif sort_by == SortBy.GOALS:
         key = sort_by_goals
        elif sort_by == SortBy.ASSISTS:
            key = sort_by_assists

        sorted_players = sorted(
            self._players,
            reverse=True,
            key=key
        )

        result=[]
        for player in sorted_players:
            if len(result)<how_many:
                result.append(player)
        return result


    
