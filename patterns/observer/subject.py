from typing import List
from .observer import Observer


class Subject:
    _observers: List[Observer]

    def register(self, observer: Observer):
        self._observers.append(observer)

    def remove(self, observer: Observer):
        self._observers.remove(observer)

    def notify(self, value):
        def update(observer: Observer): observer.update(value)

        list(map(update, self._observers))
