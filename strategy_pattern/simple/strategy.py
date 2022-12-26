from abc import ABCMeta, abstractmethod
from players import Player, create_players
from typing import List


class OrderingStrategy(metaclass=ABCMeta):
    @abstractmethod
    def create_ordering(self, player_instances_list: list) -> List[Player]:
        """Create ordering based on player statistics"""


class HighestRunsOrderingStrategy(OrderingStrategy):
    def create_ordering(self, player_instances_list):
        """Create ordering based on highest scores"""
        return sorted(player_instances_list, key=lambda x: x.runs, reverse=True)


class HighestBallsOrderingStrategy(OrderingStrategy):
    def create_ordering(self, player_instances_list):
        """Create ordering based on highest number of balls faced"""
        return sorted(player_instances_list, key=lambda x: x.balls, reverse=True)


class HighestFoursOrderingStrategy(OrderingStrategy):
    def create_ordering(self, player_instances_list):
        """Create ordering based on highest number of fours hit"""
        return sorted(player_instances_list, key=lambda x: x.fours, reverse=True)


class HighestSixesOrderingStrategy(OrderingStrategy):
    def create_ordering(self, player_instances_list):
        """Create ordering based on highest number of sixes hit"""
        return sorted(player_instances_list, key=lambda x: x.sixes, reverse=True)


class HighestStrikeRateOrderingStrategy(OrderingStrategy):
    def create_ordering(self, player_instances_list):
        """Create ordering based on highest number of sixes hit"""
        return sorted(player_instances_list, key=lambda x: x.strike_rate, reverse=True)


class HighestTimeRateOrderingStrategy(OrderingStrategy):
    def create_ordering(self, player_instances_list):
        """Create ordering based on highest number of time on crease hit"""
        return sorted(player_instances_list, key=lambda x: x.minutes, reverse=True)


def process_players(strategy: OrderingStrategy):
    players = create_players()
    print(f'***** {strategy.__class__.__name__.upper()} *****'.center(75))
    for player in strategy.create_ordering(player_instances_list=players):
        print(player)


if __name__ == '__main__':
    process_players(HighestFoursOrderingStrategy())
