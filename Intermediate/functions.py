def print_student_name(name):
    """
    This function prints the name of a student.
    """

    print("Student name is:", name)

def sub_two_numbers(num1, num2=1000):
    """
    This function returns the difference of two numbers.
    """

    total = num1 - num2
    return total


# first_name = input("Enter student name: ")
# print_student_name(first_name)

total = sub_two_numbers(5, 10)
print(total)

print(sub_two_numbers(5))
print(sub_two_numbers(50, 5))
print(sub_two_numbers(num2=50, num1=5))


