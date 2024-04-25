from itertools import permutations

x = "ABC"
perms = permutations(x)

for perm in perms:
    print(''.join(perm))
