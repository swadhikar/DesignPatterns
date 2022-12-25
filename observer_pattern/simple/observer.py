class Publisher:
    """Concrete Observable"""

    def __init__(self):
        self._subscribers = set()

    def subscribe(self, observer):
        self._subscribers.add(observer)

    def unsubscribe(self, observer):
        self._subscribers.discard(observer)

    def notify_subscribers(self, message):
        for subscriber in self._subscribers:
            subscriber.notify(message)


class Subscriber:
    """Concrete observer"""

    def __init__(self, name):
        self.name = name

    def notify(self, data):
        print(f'Subscriber: {self.name} got: {data}')
