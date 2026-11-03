def logout(current_user):

    if current_user:
        print("Logout successful")
        return None
    else:
        print("No user is logged in")
        return None

