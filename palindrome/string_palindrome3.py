#String palindrome problem can be solved using two pointers
def is_palindrome(s):
    left = 0
    right = len(s)-1
    while left < right:
        if s[left] != s[right]:
            return False
        left = left + 1
        right = right -1
    return True

def main():
    test_cases = ["RACEACAR", "A", "ABCDEFGFEDCBA",
                  "ABC", "ABCBA", "ABBA", "RACEACAR"]
    largest_palindrome = None
    smallest_palindrome = None

    for i in range(len(test_cases)):
        print("test case #", i + 1)
        print("_" * 100)
        print("The Input string is ", test_cases[i], " and the lenght of the string is ", len(test_cases[i]), ".", sep="")
        print("is palindrome...", is_palindrome(test_cases[i]))

        if is_palindrome(test_cases[i]) is None or len(test_cases[i]) > len(test_cases):
            largest_palindrome = test_cases[i]
        if is_palindrome(test_cases[i]) is None or len(test_cases[i]) < len(test_cases):
            smallest_palindrome = test_cases[i]
            
            print("smallest_palindrome is :", smallest_palindrome)
            print("largest_palindrome is :", largest_palindrome)
            
        print("_" * 100)


if __name__ == '__main__':
    main()