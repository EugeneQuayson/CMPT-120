import random


class Student:
    def __init__(self, name, student_id, year, major, gpa):
        self.name = name
        self.student_id = student_id
        self.year = year
        self.major = major
        self.gpa = float(gpa)

    def honors(self):
        if self.gpa > float(3.5):
            return True
        else:
            return False

    def free(self):
        winning_number = random.randint(1, 10)
        if winning_number == self.student_id:
            return "Winner!", self.name, "gets free lunch!"
        else:
            return "Loser!"


def main():
    student1 = Student("Dylan", 1, "Freshman", "Comp Sci", float(3.6))
    student2 = Student("Oscar", 2, "Sophomore", "Business", float(3.3))
    student3 = Student("Daniel", 3, "Junior", "Dev Sci", float(2.5))
    print(student1.name, student1.honors(), student1.free())
    print(student2.name, student2.honors(), student2.free())
    print(student3.name, student3.honors(), student3.free())


main()
