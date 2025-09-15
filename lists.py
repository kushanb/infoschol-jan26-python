list1 = [1, 2, 3, 4, 5]
list2 = ["apple", "banana", "cherry"]
list3 = [1, "apple", 3.5, True]

print(list1)
print(list2)
print(list3)
print(list1[0])  # Accessing first element
print(list2[1:3])  # Slicing list2 from index 1 to 2
print(list3[::-1])  # Reversing list3

list2.append("date")  # Adding an element to list2
print(list2)
list2.remove("banana")  # Removing an element from list2
print(list2)