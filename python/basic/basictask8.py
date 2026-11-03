students = {}

def signup():
    id = input("enter student id: ")
    email = input("enter email: ")
    password = input("enter password: ")

    if id == "" or email == "" or password == "":
        print("Enter all details")
        return

    if "@" not in email:
        print("Invalid email")
        return

    if len(password) < 6:
        print("invalid password")
        return

    students[id] = {
        "email": email,
        "password": password
    }

    print("signup successful")


def login():
    email = input("enter email: ")
    password = input("enter password: ")

    if email == "" or password == "":
        print("Enter all information")
        return

    for id, student in students.items():
        if student["email"] == email and student["password"] == password:
            print("Login successful")
            return

    print("wrong email or password")


while True:
    print("\n--- STUDENT MENU ---")
    print("1. Signup")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        signup()
    elif choice == "2":
        login()
    elif choice == "3":
        print("Goodbye")
        break
    else:
        print("Invalid choice")




