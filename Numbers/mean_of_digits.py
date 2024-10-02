def mean_digit(num):
    sum_digit = 0
    count_digit = 0
    for digit in str(num):
        sum_digit += int(digit)
        count_digit += 1
    return sum_digit/count_digit
num = 12341
print(mean_digit(num))