class Student:
    def __init__(ikra, name, age, grade):
        ikra.name = name
        ikra.age = age
        ikra.grade = grade

name = input("Enter student name: ")
age = int(input("Enter student age: "))
grade = input("Enter student grade: ")

s1 = Student(name, age, grade)

print("Name:", s1.name)
print("Age:", s1.age)
print("Grade:", s1.grade)