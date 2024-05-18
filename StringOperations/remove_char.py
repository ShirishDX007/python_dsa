name = "girish"

char_list = list(name)

index = name.find('i')

if index != -1:
    del char_list[index]

modified_name = ''.join(char_list)
print(modified_name)

# text = "girish"
# replace_text = text.replace('i', "")
# print(replace_text)