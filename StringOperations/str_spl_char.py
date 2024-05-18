def plain_text(s):
    new_list = []
    for i in s:
        if i.isalnum():
            new_list.append(i)
    return new_list
str = "76a68-34b'2b3#449sc-99"
result = plain_text(str)

str_join = ''.join(result)
print("String after removing spacial charecters.")
print(str_join)