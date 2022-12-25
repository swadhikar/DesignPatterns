from concrete import Observable, Observer

if __name__ == '__main__':
    observable = Observable()
    observer_1 = Observer('A', observable)
    observer_2 = Observer('B', observable)

    observable.monitor(1, 2, 3, company='ABC')
