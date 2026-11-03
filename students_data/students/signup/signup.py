from validation.validation import check_email,check_name,check_password
students={}
def signup():
    name=input("enter your name:")
    while not check_name(name):
        print("name cannot be empty")
        name=input("enter your name:")
    email=input("enter your email:")

    while not check_email (email):
        print("invalid email")
        email=input("enter your email:")
        if email in students:
            print("email already exixts")
            return

    password=input("enter your password:")
    while not check_password(password):
        print("password must be at least 6 characters")
        password=input("enter your password")

    students[email]={
        "name":name,
        "email":email,
        "password":password
    }

    print("signup successful")