student = {
    "name": "John Doe",
    "age": 21,
    "courses": ["Math", "Science", "History"],
    "is_active": True,
    "address": {
        "street": "123 Main St",
        "city": "Anytown",
        "zip": "12345"  
    }
}

# print(student["address"]["city"])

print(student.keys())
for key in student.keys():
    print(key, ":", student[key])

print(student.get("name"))

student[0] = "New Value"
print(student)
student["age"] = 22
print(student)

student.pop(0)
print(student)