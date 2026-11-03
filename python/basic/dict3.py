dict = {
    "name": "ikra",
    "password": "123456",
    "email": "ikra@gamil.com",
}
   
def login():
    password = input("password: ")
    email = input("email: ")

    if password == dict["password"] and email == dict["email"]:
        print("successfully")
    else:
        print("invalid")

login()

