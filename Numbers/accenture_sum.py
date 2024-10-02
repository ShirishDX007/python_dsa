
#write Pseudocode for following program
# 1. Create three lists: names1, names2, and names3.
# 2. Initialize names2 to be a reference to names1.
# 3. Initialize names3 to be a copy of names1.
# 4. Change the first element of names2 to 'Alice'.
# 5. Change the second element of names3 to 'Bob'.
# 6. Initialize a variable sum to 0.
# 7. Iterate through the lists names1, names2, and names3.
# 8. For each list, check if the first element is 'Alice'. If it is, add 1 to sum.
# 9. For each list, check if the second element is 'Bob'. If it is, add 10 to sum.
# 10. Print the value of sum.

names1 = ['Amir', 'Bear', 'Charlton', 'Daman']
names2 = names1
names3 = names1[:]

names2[0] = 'Alice'
names3[1] = 'Bob'

sum = 0
for ls in (names1, names2, names3):
    if ls[0] == 'Alice':
        sum += 1
    if ls[1] == 'Bob':
        sum += 10

print(sum)