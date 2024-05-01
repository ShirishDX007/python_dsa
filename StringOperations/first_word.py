import string
sentence = "Hello's there, how are you"
clean_sen = sentence.translate(str.maketrans('', '', string.punctuation))
words = clean_sen.split()
print(words[0])


