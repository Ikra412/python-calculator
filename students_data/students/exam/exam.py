def exam():
    print("exam details")
    name=input("exam name:")
    subject=input("subject name:")
    marks=int(input("enter marks:"))

    data={
        "name":name,
        "subject":subject,
        "marks":marks
    }

    print(data)