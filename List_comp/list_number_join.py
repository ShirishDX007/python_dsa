list_nums = [1,2,3,4,5]

def join_nums(list_nums):
    new_list = ''.join(map(str, list_nums))
    return int(new_list)

joined_nums = join_nums(list_nums)
print(joined_nums)