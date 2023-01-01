from classes import MovieFactory

if __name__ == '__main__':
    # Invoke the factory to get meaningful instances
    instances = MovieFactory.get_instances(
        'Taanakkaran',
        'Sila Nerangalil Sila Manidhargal',
        'Thiruchitrambalam'
    )

    for inst in instances:
        print('*****************************************************')
        print(f'Movie        : {inst.movie}')
        print(f'IMDB rank    : {inst.rank}')
        print(f'IMDB rating  : {inst.rating}')
        print(f'Release date : {inst.year}')
        print('*****************************************************')
