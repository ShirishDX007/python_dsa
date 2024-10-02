def find_numbers(st):
    result = []
    current_substring = ""
    for char in st:
        if char != "/":
            current_substring += char
        else:
            result.append(current_substring + str(len(current_substring)))
            current_substring = ""
    if current_substring:
        result.append(current_substring + str(len(current_substring)))

    return ''.join(result)
st = "aba/djdjdj/scd/eresfa/"
modified_string = find_numbers(st)
print(modified_string)