from abc import ABC, abstractmethod


# Prototype
class Person(ABC):
    @abstractmethod
    def clone(self):
        pass

    @abstractmethod
    def display(self):
        pass
