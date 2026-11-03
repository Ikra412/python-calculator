import json
student = {
    "id": input("enter your id:"),
    "name": input("Enter your name: "),
    "address": input("Enter your address: "),
    "class": input("Enter your class: "),
    "qualification": []
}

while True:
    qualification=input("enter your qualification:")
    student["qualification"].append(qualification)
    print("1. enter your choice")
    print("2. exit")
    ch=input("enter your choice:")
    if ch =="2":
        break
print(json.dumps(student,indent=4))
print(student)

