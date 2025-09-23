num = 10

# cont = True
# while cont:
#     print(num)
#     num += 1
#     if num > 20:
#         cont = False


run = True
while run:
    try:
        marks = int(input("Enter your marks: "))   
    except ValueError:
        print("Invalid input. Please enter a valid integer for marks.")
        continue  # Prompt the user to enter the marks again
    
    print(type(marks))
    if(marks >= 70):
        print("A")
    elif(marks >= 65):
        print("B")
    elif(marks >= 40):
        print("C")
    else:
        print("F")

    # Get an input to continue or stop the loop
    choice = input("Do you want to continue? (yes/no): ").strip().lower()

    # Exit the loop if the user types 'no'
    if choice == 'no':
        run = False
        print("Exiting the loop. Goodbye!")
    else:
        print("Continuing the loop.")