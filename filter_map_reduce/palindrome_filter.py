#words = ("filter", "Ana", "hello", "world", "madam", "racecar")

def is_palindrome(word):
    reversed_word = ''.join(reversed(word))
    return word.lower() == reversed_word.lower()


#list(filter(is_palindrome, words))