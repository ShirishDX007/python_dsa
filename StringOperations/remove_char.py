name = "girish"

char_list = list(name)

index = name.find('r')

if index != -1:
    del char_list[index]

modified_name = ''.join(char_list)
print(modified_name)