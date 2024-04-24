num_list1 = [10,23,66,15,12]
num_list2 = [12,24,65,17,52]

#List Comprehension [expression for loop if condition]

sum_list = [(n1 + n2) for n1 in num_list1 for n2 in num_list2 if n1 + n2 >100 ]
print(sum_list)
#print(num_doubles)

