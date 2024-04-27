#List Comprension to create new list [expression for loop condition]
nums = [2,4,5,6, 8]
print(f"List of numbers: {nums}")

print("Multiplication")
x = [num * 2 for num in nums ]
print(f"x: ", x)

print("Addition")
y = [num + 2 for num in nums]
print(f"y:" ,y)

z = [num -2 for num in nums]
print(f"z:" ,z)
