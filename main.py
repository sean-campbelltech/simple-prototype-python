from teacher import Teacher
from student import Student


# Client
def main():
    teacher = Teacher("Sean Campbell", "Creational Design Pattern in Python")
    teacherClone = teacher.clone()
    teacherClone.display()

    student = Student("James Bond", teacherClone)
    studentClone = student.clone()
    studentClone.display()

    # modify teacher clone
    teacherClone.set_course("Python Programming Course")
    studentClone.display()


if __name__ == "__main__":
    main()
