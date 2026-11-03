students = {
    "ikra@gmail.com": {
        "name": "ikra",
        "address": "jodhpur",
        "password": "123456"
    },

    "afrin@gmail.com": {
        "name": "afrin",
        "address": "jaipur",
        "password": "654321"
    },

    "jyoti@gmail.com": {
        "name": "jyoti",
        "address": "ajmer",
        "password": "56789"
    }
}

def login():
    email = input("Enter email: ")
    password = input("Enter password: ")

    if email in students:
        if students[email]["password"] == password:
            print("Successfully Login")
            print("Name:", students[email]["name"])
        else:
            print("Invalid Password")
    else:
        print("Email not found")


login()