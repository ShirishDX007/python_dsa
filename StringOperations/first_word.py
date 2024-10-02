import string
sentence = "Hello's there, how are you"
clean_sen = sentence.translate(str.maketrans('', '', string.punctuation))
words = clean_sen.split()
print(words[0])

def find_vowel_words(sentence):
    vowels = []
    words = sentence.split()
    for i in words:
        if i[0] in "aeiouAEIOU":
            vowels.append(i)
    return vowels



