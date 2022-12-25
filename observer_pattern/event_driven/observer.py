class Publisher:
    """Concrete Observable"""

    SUBSCRIBERS = {}

    @classmethod
    def subscribe(cls, event, observer):
        """Subscribe to an event"""
        cls.SUBSCRIBERS[event] = cls.SUBSCRIBERS.get(event, set())
        cls.SUBSCRIBERS[event].add(observer)
        print(f'{observer} subscribed to "{event}" event')

    @classmethod
    def unsubscribe(cls, event, observer):
        """Unsubscribe from an event"""
        cls.SUBSCRIBERS[event].discard(observer)
        print(f'{observer} unsubscribed from "{event}" event')

    def notify_subscribers(self, event, message):
        """Notifies the subscribers with message"""
        for subscriber in self.SUBSCRIBERS[event]:
            subscriber.notify(message)


class Subscriber:
    """Concrete observer"""

    def __init__(self, name, event):
        self.name = name
        Publisher.subscribe(event, self)

    def notify(self, data):
        print(f'subscriber: "{self.name}" got: {data}')

    def __repr__(self):
        return self.name
