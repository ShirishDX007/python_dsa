#lambda often used with map why?
""" map function takes a function and iterable as an arguments. 
It then applies provided function to each element of the iterable and 
returns a new iterable with result."""

x = [3, 4, 1, 6, 8]
multiplication = list(map(lambda x: x * 2, x))
print("lambda with map function:", multiplication)

print("_"*50)

#lambda with filter
nums = range(52, 101)
even_nums = list(filter(lambda x: x % 2 == 0, nums))
print(":lambda with filter function:",even_nums)


print("_"*50)

#lambda with reduce function
""" reduce apply function to two arguments cumilatively to the items of sequence or 
    iterable from left to right and return a single value.""" 
from functools import reduce
sales = [123, 112, 101, 104]
total_sales = reduce(lambda x,y: x + y, sales)
print(" lambda with reduce function:",total_sales)