#write a function to calculate mean of digits , number rounded to two decimal
def mean_of_digits(numbers):
    #convert digits to string
    digits = str(numbers)
    #convert string back to digit and create a list
    digit_list = [int(numbers) for numbers in digits]

    sum_of_num = sum(digit_list)/ len(digit_list)
    return round(sum_of_num, 2)

if __name__ == '__main__':
    numbers = 12345
    mean_digits = mean_of_digits(numbers)
    
    print(mean_digits)