#find the numbers from list whos sum equals sum_num
nums = [1,2,3,4,5,6,7,8,9,5,11,12,-1]
sum_num  = 10
def list_nums(nums, sum_num):
    result = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == sum_num:
                c = (nums[i], nums[j])
                result.append(c)
    return result
new_list = list_nums(nums, sum_num)
print(new_list)
