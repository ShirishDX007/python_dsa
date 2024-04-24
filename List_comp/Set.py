odd_list = [1,2,3,4,5]
unordered_set = {3,4,5,2,2,5,2,56,4}

print(unordered_set)

for num in unordered_set:
    if(not num % 2 == 0 ):
        odd_list.append(num)

print(odd_list)
