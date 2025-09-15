# age = 17
# if age >= 18:
#     print("You are eligible to vote.")
# else:
#     print("You are not eligible to vote.")

# age = 15

# if(age >= 18):
#     print("You're an adult.")
# elif(age < 18 and age >= 13):
#     print("You're a teenager.")
# else:
#     print("You're a child.")


marks = int(input("Enter your marks: "))   
print(type(marks))
if(marks >= 70):
    print("A")
elif(marks >= 65):
    print("B")
elif(marks >= 40):
    print("C")
else:
    print("F")