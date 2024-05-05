def is_palindrome(word):
    word = ''.join(e for e in word if e.isalnum()).lower()
    return word == word[::-1]

def smallest_largest_palindrome(input_string):
    words = input_string.split()

    smallest_palindrome = None
    largest_palindrome = None

    for word in words:
        if smallest_palindrome is None or word > smallest_palindrome:
            smallest_palindrome = word
        if largest_palindrome is None or word < largest_palindrome:
            largest_palindrome = word

    return smallest_palindrome, largest_palindrome

input_string = "You abbba abcded own wow kayak"
smallest, largest = smallest_largest_palindrome(input_string)
print(f"smallest palindrome ", smallest)
print("largest palindrome ", largest)
