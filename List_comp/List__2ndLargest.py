my_list = [2,1,4,3,8,9,7]

max_number = max(my_list)

def second_largest(my_list):
    my_list.remove(max(my_list))
    return max(my_list)

if __name__ == '__main__':
    second_highest_number = second_largest(my_list.copy())
    print("Original list: ", my_list)
    print("Sorted List: ", sorted(my_list))
    print("_"*100)
    print("Method one: ")
    print("max number: ", max_number)
    print("second highest number: ", second_highest_number)
    print("_"*100)    

sorted_list = sorted(my_list, reverse=True)[1]
sorted_my_list = sorted(my_list)[-2]
Third_highest = sorted(my_list)[-3]
print("Method Two: ")
print("second_highest number from reverse sorted list: ", sorted_list)
print("second_highest number from sorted list: ", sorted_my_list)
print("Third_highest number from sorted list: ", Third_highest)

print("_"*100)
