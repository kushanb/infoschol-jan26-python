string1 = "Hello"
string2 = 'World'

string3 = "Don't worry about apostrophes"
string4 = 'don\'t worry about apostrophes'

print(string1)
print(string2)
print(string3)
print(string4)

# Extract substring from string3 starting at index 3 to the end
print(string3[3:]) 
# Extract substring from string4 starting at the beginning up to but not including index 4
print(string4[:4])
# Extract substring from string4 starting at index 1 up to but not including index 7, taking every 2nd character
print(string4[1:7:2])
# Reverse string4
print(string4[::-1])


print(string1, string2) # Print string1 and string2 separated by a space
print(string1 + " ... " + string2) # Concatenate string1 and string2 with a space in between
print(string1 * 3) # Print string1 three times in a row

print(string1.upper()) # Convert string1 to uppercase
print(string2.lower()) # Convert string2 to lowercase
print(string1.replace("H", "J")) # Replace 'H' with 'J'
print(string4.capitalize()) # Capitalize the first letter of string1