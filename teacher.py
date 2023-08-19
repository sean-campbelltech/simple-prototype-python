import copy
from person import Person


class Teacher(Person):
    def __init__(self, name: str, course: str):
        self._name = name
        self._course = course

    def clone(self):
        return copy.copy(self)

    def display(self):
        print("Teacher was cloned:")
        print(f"Teacher Name: {self._name}")
        print(f"Who Teaches: {self._course}\n")

    def get_name(self):
        return self._name

    def set_name(self, name: str):
        self._name = name

    def get_course(self):
        return self._course

    def set_course(self, course: str):
        self._course = course
