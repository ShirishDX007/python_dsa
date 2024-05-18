#find odd numbers from number 4 to 25
nums = list(range(4,26))
mapped_nums = list(map(lambda n: n,nums))
print(mapped_nums)
odd_numbers= list(filter(lambda x: x % 2, mapped_nums))
print("Odd numbers are: ", odd_numbers)

#find even number from 10 number and multiples of 8
#numbers = list(range(0,11))
even_nums = [num for num in range(11) if num % 2 == 0 ]
eight_nums = [ n for n in range(11) if n % 8 == 0]
print("Even numbers are: ", even_nums)
print("Eight numbers are: ", eight_nums)