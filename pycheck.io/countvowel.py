def count_vowels(text: str) -> int:
    vowels = ['a','e', 'i', 'o', 'u']
    count = 0
    for char in text:
        if char.lower() in vowels:
            count += 1
    return count
    
# alternate method is sum(text.lower().count(i) for i in "aeiou")

print("Example...")
print(count_vowels("Hello"))

#self check the text with count vowels method
assert count_vowels("hello") == 2
assert count_vowels("mango") == 2
assert count_vowels("oRANGE") == 3
assert count_vowels("shirish") == 2
assert count_vowels("a") == 1
assert count_vowels("b") == 0
assert count_vowels("aeiou") == 5
assert count_vowels("AEIOU") == 5
assert count_vowels("The quick brown fox") == 5
assert count_vowels("Jumps over the lazy dog") == 6
assert count_vowels("") == 0

