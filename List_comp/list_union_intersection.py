list1 = [1,2,3,4]
list2 = [3,4,5,6,7]

def union_intersection(list1, list2):
    union = sorted(list(set(list1) | set(list2)))
    intersection = sorted(set(list1) & set(list2))
    return (union, intersection)

new_list =  union_intersection(list1, list2)
print(new_list)