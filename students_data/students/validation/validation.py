def check_name(name):
    if name.strip()=="":
        return False
    return True

def check_email(email):
    if "@" in email and "." in email:
        return True
    return False

def check_password(password):
    if len(password) >=6:
        return True
    return False

def check_marks(marks,total):
    if 0 <=marks <=total:
        return True
    return False

def check_fees(paid,total):
    if 0 <=paid <=total:
        return True
    return False
    


    