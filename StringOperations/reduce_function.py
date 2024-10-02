#reduce(function, iterable)
#reduce : apply a rolling computation to pair of values
from functools import reduce
list_of_lists = [[1,2,3], [4,5,6,], [9,4,2]]
flattened_list = reduce(lambda x,y : x + y, list_of_lists)
print(flattened_list)
print("_"*50)
input_string = "a quick brown frog jumped over the lazy dog."
def longest_word(input_string):
    word = reduce(lambda x,y: x if len(x) > len(y) else y, input_string.split())
    return word
print(longest_word(input_string))
print("_"*50)

