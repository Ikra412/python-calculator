from signup.signup import students

def login():
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    if email in students:
        if students[email]["password"] == password:
            print("Login successful")
            return students[email]
        else:
            print("Wrong password")
    else:
        print("Email not registered")

    return None
    





    
    
    
    

    