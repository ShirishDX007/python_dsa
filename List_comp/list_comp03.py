#List comprehension for function calls
print("print the length of word from sentence.")
sentence = " The quick green frog jump over the dog."
y = [ len(word) for word in sentence.split()]

print(y)

print("_" * 100)
#fillter with List comprehension
even_numbers = [x for x in range(10) if x % 2 == 0]

print(even_numbers)
print("_" * 100)
#2D matrix in list comprehension
matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
]
x = [[row[i] for row in matrix] for i in range(4)]

print("Transpose of 2D matrix..")
print(x)
print("_" * 100)