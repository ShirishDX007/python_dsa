#generator expression is a consise way to create a generator object
#generator expression (expression for item in iterable)

squares_generator = (i * i for i in range(5))

for val in squares_generator:
    print(val)
