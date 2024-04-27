def  longest_word(sentence : str)-> str:
    max_length = 0
    longest = ""
    for word in sentence.split():
        #print(word)
        if (len(word) > max_length):
                max_length = len(word)
                longest = word.lower()
    return longest
#alternet solution to above method is max(sentence.split(), key=len , default="")

longest = longest_word("brown frog dragonbooster")
print(longest)

assert longest_word("openai gpt-4") == "openai" 
assert longest_word("the answer is 42") == "answer"
assert longest_word("hello martini") == "martini"
assert longest_word("typescript is great") == "typescript"
assert longest_word("the answer is 42") == "answer"
assert longest_word("to be or not to be") == "not"
assert longest_word("that is the question") == "question"
assert longest_word("") == ""
print ("ok")

