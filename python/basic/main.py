from calculator import calculator
while True:
    print("calculator")
    print("exit")

    choice=int(input("enter your choice"))
    if choice==1:
        calculator()
    elif choice==2:
        break
    else:
        print("invalid choice:")

calculator()



