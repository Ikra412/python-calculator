import json
from datetime import datetime, date

def signup():
    with open("data.json", "r") as file:
        data = json.load(file)

    name = input("enter your name: ")
    email = input("enter your email: ")
    username = input("enter your username: ")
    password = input("enter your password: ")

    if name == "" or email == "" or username == "" or password == "":
        print("Please enter all details.")
        return

    if not name.replace(" ", "").isalpha():
        print("Please enter a valid name.")
        return

    if "@" not in email or "." not in email:
        print("Invalid email.")
        return

    if len(password) < 6:
        print("Password must be at least 6 characters.")
        return

    for student in data:
        if student["username"] == username:
            print("username already exists")
            return

    qualifications = input(
        "Enter qualifications separated by comma: "
    ).split(",")

    qualifications = [q.strip() for q in qualifications if q.strip()]

    if not qualifications:
        print("Please enter qualification.")
        return

    now = datetime.now()
    signup_date = now.date()
    signup_time = now.time()

    student = {
        "name": name,
        "email": email,
        "username": username,
        "password": password,
        "qualifications": qualifications,
        "date": str(signup_date),
        "time": signup_time.strftime("%H:%M:%S")
    }

    data.append(student)

    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)

    print("signup successful")


def login():
    with open("data.json", "r") as file:
        data = json.load(file)

    username = input("enter your username: ")
    password = input("enter your password: ")

    for student in data:
        if student["username"] == username and student["password"] == password:
            print("login successful")
            print("welcome", student["name"])
            print("qualifications:", student["qualifications"])
            return

    print("invalid username or password")


def search_student():
    with open("data.json", "r") as file:
        data = json.load(file)

    name = input("enter student name: ").strip().lower()
    found = False

    for student in data:
        if name in student["name"].lower():
            print("student found")
            print("name:", student["name"])
            print("email:", student["email"])
            print("username:", student["username"])
            print("qualifications:", student["qualifications"])
            print("date:", student.get("date", "N/A"))
            print("time:", student.get("time", "N/A"))
            found = True

    if not found:
        print("student not found")


while True:
    print("\n1. Signup")
    print("2. Login")
    print("3. Search student")
    print("4. Exit")

    choice = input("enter your choice: ")

    if choice == "1":
        signup()
    elif choice == "2":
        login()
    elif choice == "3":
        search_student()
    elif choice == "4":
        break
    else:
        print("invalid choice")
