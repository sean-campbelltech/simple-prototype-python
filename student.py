import copy
from person import Person
from teacher import Teacher


# ConcretePrototype2
class Student(Person):
    def __init__(self, name: str, teacher: Teacher):
        super().__init__(name)
        self._teacher = teacher

    def clone(self):
        return copy.deepcopy(self)

    def display(self):
        print("Student was cloned:")
        print("-------------------")
        print(f"Student Name: {self._name}")
        print(f"Enrolled in: {self._teacher.get_course()}")
        print(f"Taught by: {self._teacher.get_name()}\n")
