# end = 100
# for i in range(2, end + 1):
#     if(i % 3 == 0):
#         print(i)

for j in range(1, 25):
    if (j % 3 == 0):
        continue
    elif(j == 23):
        break
    print(j)