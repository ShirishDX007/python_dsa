from collections import defaultdict

sentence = " the red rabbit jumped over the red fox and ran way into the forest"
words = sentence.split()
d = defaultdict(int)
for word in words:
    d[word] += 1
print(d)

my_list = [(1234, 100.23), (345, 10.45), (1234, 75.00),
           (345, 222.66), (678, 300.25), (1234, 35.67)]

dt = defaultdict(list)
for acct_num, value in my_list:
    dt[acct_num].append(value)

print("converted list to dictionary:", dt)
# Summing up the values for each acct_num
sum_dt = {acct_num: sum(values) for acct_num, values in dt.items()}
print(sum_dt)

#Using lambda as the default_factory
""" This will assign monkey as the default value for any key that is not present in the dictionary"""
animal = defaultdict(lambda: "Monkey")
animal['sam'] = 'Tiger'
print(animal['mafia'])
print(animal)

print("_"*100)

sentence = "How much wood would a woodchuck chuck if a woodchuck would chuck wood ?"
words = sentence.split(" ")
d = defaultdict(int)
for word in words:
    d[word] = 1
print(d[1])
