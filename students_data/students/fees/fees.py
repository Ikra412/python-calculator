def fees():
    print("student fees")

    total=int(input("enter total fees:"))
    paid=int(input("enter paid fees:"))

    remaining=total-paid
    print("remaining fees:",remaining)