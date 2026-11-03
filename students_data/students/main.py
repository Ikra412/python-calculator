from menu import menu
from signup.signup import signup
from login.login import login
from profile.profile import profile
from course.course import course
from search.search import search
from fees.fees import fees
from attendance.attendance import attendance
from result.result import result
from exam.exam import exam

user=None
while True:
    choice = menu()

    if choice == "1":
        signup()
    elif choice == "2":
        user=login()
    elif choice == "3":
        if user:
            profile(user)
        else:
            print("please login first")     
    elif choice == "4":
        course()
    elif choice == "5":
        search()
    elif choice == "6":
        fees()
    elif choice == "7":
        attendance()
    elif choice == "8":
        result()
    elif choice == "9":
        exam()
    elif choice == "10":
        print("Logout selected")
    elif choice == "11":
        print("Thank you")
        break
    else:
        print("Invalid choice")

