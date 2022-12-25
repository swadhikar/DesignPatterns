from abc import ABCMeta, abstractmethod


class IObservable(metaclass=ABCMeta):
    @abstractmethod
    def subscribe(self, observer):
        """Subscribe"""

    @abstractmethod
    def unsubscribe(self, observer):
        """Unsubscribe"""

    @abstractmethod
    def monitor(self, observer):
        """Unsubscribe"""


class IObserver(metaclass=ABCMeta):
    @abstractmethod
    def notify(self):
        """Notifies the observer"""
