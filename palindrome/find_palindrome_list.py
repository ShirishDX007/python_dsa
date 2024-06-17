my_string = "abaGADAGdata"

def find_palindrome(my_string):
    result = []
    for i in range(len(my_string)):
        for j in range(i, len(my_string)):
            substring = my_string[i:j+1]
            if substring == substring[::-1]:
                result.append(substring)

    return result
print(find_palindrome(my_string))
