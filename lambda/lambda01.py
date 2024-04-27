callables = []
for i in range(5):
    callables.append(lambda a=i: a )
    
for f in callables:
    print(f())