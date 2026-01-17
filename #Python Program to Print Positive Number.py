# First input list
list1 = [12, -7, 5, 64, -14]
print("Input:", list1)
print("Output:", end=" ")

for num in list1:
    if num > 0:
        print(num, end=", ")

print("\n")

# Second input list
list2 = [12, 14, -95, 3]
print("Input:", list2)

positive_numbers = []
for num in list2:
    if num > 0:
        positive_numbers.append(num)

print("Output:", positive_numbers)
