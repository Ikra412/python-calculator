def signup(user):
    name = input("Enter name: ")
    password = input("Enter password: ")

    user[name] = password

    print("Signup successful")


