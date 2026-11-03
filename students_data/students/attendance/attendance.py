def attendance():
    print("student attendance")
    total_days=int(input("enter total days:"))
    present_days=int(input("enter present days:"))

    absent_days=total_days-present_days
    print("present days:",present_days)
    print("absent days:",absent_days)