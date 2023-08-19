from abc import ABC, abstractmethod


class Person(ABC):
    @abstractmethod
    def clone(self):
        pass

    @abstractmethod
    def display(self):
        pass
