import copy
from person import Person
from teacher import Teacher


class Student(Person):
    def __init__(self, name: str, teacher: Teacher):
        self._name = name
        self._teacher = teacher

    def clone(self):
        return copy.deepcopy(self)

    def display(self):
        print("Student was cloned:")
        print("-------------------")
        print(f"Student Name: {self._name}")
        print(f"Enrolled in: {self._teacher.get_course()}")
        print(f"Taught by: {self._teacher.get_name()}\n")
