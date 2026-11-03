def calculator():
    a = int(input("enter your first value: "))
    b = int(input("enter your second value: "))

    print("1.add:")
    print("2.sub:")
    print("3.multi:")
    print("4.divid:")

    choice = int(input("enter your choice: "))

    if choice == 1:
        print(a + b)
    elif choice == 2:
        print(a - b)
    elif choice == 3:
        print(a * b)
    elif choice == 4:
        print(a / b)
    else:
        print("invalid choice:")

