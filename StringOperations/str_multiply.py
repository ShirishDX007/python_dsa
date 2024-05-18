#Multiply integers with string charecters
def mul_string(s):
    str_list = list(s)
    re = ""
    for i in range(len(list(str_list))):
        if str_list[i].isalpha():
            re += str_list[i] * int(str_list[i + 1])
    return re
str = "x3y4b2f3z2"
print("Origanl string", str)
remove_int = [x for x in str if not x.isdigit()]
remove_str = [x for x in str if  x.isdigit()]
print("string after removing integers: ",remove_int )
print("string after removing string: ",remove_str )

new_string = mul_string(str)
print("string char multiples of numbers are: ",new_string)