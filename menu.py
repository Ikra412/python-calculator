import student_mangement

user = {}
current_user = None

while True:

    print("\n----- MENU -----")
    print("1. Signup")
    print("2. Login")
    print("3. Logout")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        student_mangement.signup(user)

    elif choice == "2":
        current_user =student_mangement.login(user)

    elif choice == "3":
        current_user =student_mangement.logout(current_user)

    elif choice == "4":
        print("Thank you")
        break

    else:
        print("Wrong choice")



