def login(user):

    name = input("Enter name: ")
    password = input("Enter password: ")

    if name in user and user[name] == password:
        print("Login successful")
        return name
    else:
        print("Wrong name or password")
        return None

