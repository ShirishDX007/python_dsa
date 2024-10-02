def reverse_words(s):
    # Split the string into words
    words = s.split()
    # Reverse the list of words
    reversed_words = [word for word in words[::-1]]
    # Join the reversed words into a single string
    return ' '.join(reversed_words)

# Test the function
s = "the sky is blue"
print(reverse_words(s))