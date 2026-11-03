from calculator.add import add
from calculator.subtract import subtract
from calculator.multiply import multiply
from calculator.divide import divide
from calculator.modulus import modulus

while True:
    print("1..add")
    print("2..subtract")
    print("3..multiply")
    print("4..divide")
    print("5..modulus") 
    choise=int(input("enter your choise:"))
    if choise==1:
        a=int(input("enter your value a:"))
        b=int(input("enter your value b:"))
        print(add(a,b))
    elif choise==2:
        a=int(input("enter your value a:"))
        b=int(input("enter your value b:"))
        print(subtract(a,b))
    elif choise==3:
        a=int(input("enter your value a:"))
        b=int(input("enter your value b:")) 
        print(multiply(a,b))
    elif choise==4:
        a=int(input("ener your value a:"))
        b=int(input("enter your value b:"))
        print(divide(a,b))
    elif choise==5:
        a=int(input("enter your value a:"))
        b=int(input("enter your value b:"))
        print(modulus(a,b))
    elif choise==6:
        break
    else:
        print("wrong choise")
                           
