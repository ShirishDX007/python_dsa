num_list = [1,3,4,2,5,4,8]
if num_list == set(num_list):
    print("Duplicates are not there.")
else:
    print("Duplicates are there.")

duplicates = [x for x in num_list if num_list.count(x) > 1]
print(duplicates)