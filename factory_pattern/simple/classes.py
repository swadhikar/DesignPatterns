from dataclasses import dataclass
from lib import (
    get_csv_data,
    enrich_data,
    # pretty_print
)

ratings_file = 'imdb.csv'
data = {}

for _dict in get_csv_data(ratings_file):
    datum = enrich_data(_dict, rank=int, year=int, rating=float)
    movie = datum['movie']
    data.update({movie: datum})

# pretty_print(data, title='Enriched data:')
print(f'CSV data parsed successfully')


@dataclass
class Movie:
    rank: int
    movie: str
    year: int
    rating: int


class MovieFactory:
    @classmethod
    def get_instances(cls, *movie_names):
        instances = []
        for _movie in movie_names:
            movie_info = data[_movie]
            movie_instance = Movie(
                movie_info['rank'],
                movie_info['movie'],
                movie_info['year'],
                movie_info['rating']
            )
            instances.append(movie_instance)
        return instances
