class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Grade:", self.grade)


name = input("Enter student name: ")
age = int(input("Enter student age: "))
grade = input("Enter student grade: ")

s1 = Student(name, age, grade)

s1.display_info()