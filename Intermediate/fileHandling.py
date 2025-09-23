file = open("sample.txt", "a")
file.write("Hello, World 3!\n")
file.write("This is a sample file 3.\n")
file.close()

file2 = open("sample.txt", "r")
content = file2.readlines()

for line in content:
    print(line, end="-----")
file2.close()

with open("sample.txt", "r") as file3:
    content2 = file3.read()
    print(content2)

file3 = open("output.txt", "a")
for i in range(5):
    for j in range(i):
        print("*", end="", file=file3)
    print("\n")
file3.close()

