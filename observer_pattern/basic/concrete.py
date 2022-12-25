from observer_pattern.basic.observable import IObservable, IObserver


class Observable(IObservable):
    def __init__(self):
        self._observers = set()

    def subscribe(self, observer):
        self._observers.add(observer)

    def unsubscribe(self, observer):
        self._observers.remove(observer)

    def monitor(self, *args, **kwargs):
        import time
        iterations = len(args)
        for iteration in range(iterations):
            _args = args[:iteration + 1]
            for observer in self._observers:
                observer.notify(*_args, **kwargs)
            time.sleep(0.5)


class Observer(IObserver):

    def __init__(self, name, observable):
        self.name = name
        observable.subscribe(self)

    def notify(self, *args, **kwargs):
        print(f'Observer {self.name} received: {args}, {kwargs}')
