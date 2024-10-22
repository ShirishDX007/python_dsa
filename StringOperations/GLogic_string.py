#Add pseudocode for the below program
#define a function to add a number between string with one parameter
#create an empty list of result
#create an empty string for current substring
#Iterate through the string for each char
#Inside the for loop check if char is not '/'
#add char to current string
#append the currentstring plus len of current string to the result
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