from collections import Counter

print(Counter('superduperspreadsheet'))

""" Counter.elements() returns an iterator over elements repeating each as many times as its count. 
Elements are returned in arbitrary order. If an element’s count is less than one, elements() will ignore it. """
print(list(Counter('superduperspreadsheet').elements()))

print(Counter('superduperspreadsheet').most_common(3))

counter_one = Counter('superduperspreadsheet')  
print(counter_one)
counter_two = Counter('superduper')

print(counter_one.subtract(counter_two))
print(counter_one)