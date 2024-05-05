def generator_func(n):
    value  = 0
    while value < n:
        yield value
        value += 1

val = generator_func(4)
print(val)

#for val in generator_func(5):
    #print(val)