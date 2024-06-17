#write a function to find a number comes twice in a list and the number that is missing from a sequence of numbers from 1 to n
def find_mismatch_of_number(nums):
    n = len(nums)
    expected_sum = n * (n + 1)//2
    expected_sum_of_sq = n * (n + 1) * (2 * n + 1)//6

    actual_sum = sum(nums)
    actual_sum_sq = sum(n * n for n in nums)

    difference = expected_sum - actual_sum
    differenc_sum_sq = expected_sum_of_sq - actual_sum_sq

    sum_dup_missing = differenc_sum_sq//difference

    duplicates = (sum_dup_missing - difference)//2
    missing = sum_dup_missing - duplicates

    return duplicates, missing

if __name__ == '__main__':
    nums = [1,2,2,4,5]
    result = find_mismatch_of_number(nums)
    print("Output: ", result)
    print("_"*100)

#alternate solution for above problem

def find_repeat_missing(numbers):
    repeat = 0
    missing = 0
    for i in range(len(numbers) + 1):
        if numbers.count(i) == 2:
            repeat = i
        elif numbers.count(i) == 0:
            missing = i
    return [repeat, missing]

numbers = [1,2,4,5,5,6]
findings = find_repeat_missing(numbers)
print("Alternate solution Output: ", findings)