from typing import List
from csv import DictReader

CSV_FILE = './data.csv'


class Player:
    """Player info"""

    def __init__(self, name, runs, balls, minutes, fours, sixes, strike_rate):
        self.name = name
        self.runs = runs
        self.balls = balls
        self.minutes = minutes
        self.fours = fours
        self.sixes = sixes
        self.strike_rate = strike_rate

    def __repr__(self):
        return f'Player<name={self.name}, runs={self.runs}, balls={self.balls}, ' \
               f'min={self.minutes}, 4s={self.fours}, 6s={self.sixes}, ' \
               f'SR={self.strike_rate}>'

    @classmethod
    def from_csv(cls, player_dict):
        """Creates a player instance based on csv input"""
        instance = cls(
            player_dict['player'],
            player_dict['runs'],
            player_dict['balls'],
            player_dict['minutes'],
            player_dict['fours'],
            player_dict['sixes'],
            player_dict['strike rate']
        )
        return instance


class CsvReader:
    @staticmethod
    def get_player_data_list(csv_file):
        data = []
        with open(csv_file) as csv_file_handler:
            for row in DictReader(csv_file_handler):
                enriched_data = {
                    'player': row['player'],
                    'runs': int(row['runs']),
                    'balls': int(row['balls']),
                    'minutes': int(row['minutes']),
                    'fours': int(row['fours']),
                    'sixes': int(row['sixes']),
                    'strike rate': float(row['strike rate'])
                }
                data.append(enriched_data)
        return data


def create_players() -> List[Player]:
    player_instances = []
    csv_data_list = CsvReader.get_player_data_list(CSV_FILE)

    for csv_dict in csv_data_list:
        player_instance = Player.from_csv(csv_dict)
        player_instances.append(player_instance)

    return player_instances
