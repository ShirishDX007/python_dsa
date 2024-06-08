word_list = ['apple', 'banana', 'date']

def sort_list_by_length(word_list):
    sorted_list = sorted(word_list, key=len)
    return sorted_list

new_list = sort_list_by_length(word_list)
print(new_list)