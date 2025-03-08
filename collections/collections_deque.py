from collections import deque
import string

#deque        list-like container with fast appends and pops on either end

d = deque(string.ascii_lowercase)
for letter in d:
    letter
d.append('bork')
print(d)
d.appendleft('test')
print(d)

d.rotate(1)
print(d)