def is_palindrome(s):
    if s==s[::-1]:
        return print(True)
    else:
        return print(False)

    return s

#alternate approach to solve palindrome

# def is_palindrome(s):
#     left = 0
#     right = len(s)-1
#     while left< right:
#         if s[left] != s[right]:
#             return False

#         left = left + 1
#         right = right -1
#     return True

def main():
    test = ["kaYak","hello","racecar","radar"]
    for i in range(len(test)):
        print("is_palindrome..",is_palindrome(test[i]))  

if __name__ == '__main__':
    main()