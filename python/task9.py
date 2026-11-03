users = []

for i in range(4):
    print(f"\nUser {i + 1}")

    name = input("Name: ")
    age = input("Age: ")
    city = input("City: ")
    phone = input("Phone: ")
    qualification = input("Qualification: ")

    user = {
        "name": name,
        "age": age,
        "city": city,
        "phone": phone,
        "qualification": qualification
    }

    users.append(user)

print("\nAll Users Data:")
print(users)