odd = []
num = int(input("Enter the max number: "))

# i = 1
# while(i <= num):
#     if(i % 2 != 0):
#         odd.append(i)
#     i += 1
# print(odd)

# Or
for i in range(num):
    if(i % 2 == 1):
        odd.append(i)

print("Odd numbers: ", odd)
