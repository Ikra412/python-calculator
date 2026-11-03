studentdata={}
print("*****STUDENT DATA 1 ******")
def add_data():
    id=input("enter your id:")
    name=input("enter your name:")
    address=input("enter your address:")
    qulaification=input("enter your qulaification:")
    studentdata[id]={
        "name":name,
        "address":address,
        "qualification":qulaification
    }


def show_data():
    print(studentdata)
    
while True:
    print("1.add data")
    print("2.show data")
    print("3.exit")
    choice=input("enter your choice:")
    if choice=="1":
        add_data()
    elif choice=="2":
        show_data()
    elif choice=="3":
        print("thank you")
        break
    else:
        print("invalid choice")        