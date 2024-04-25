#In this list comp we are printing numbers which are multiple of 10 to 100
x = [num for num in range(100) if num % 5 == 0 and num % 10 == 0]

print(x)

print("----****-----****----****----")

print("create square numbers from list")
nums = [3, 4, 5, 6, 8]
square = [num**2 for num in nums ]
print(square)

print("----****-----****----****----")

print("Reverse each string in tuple.")
abs = ("Read" ,"write" ,"read" , "write")
strx =  [string[::-1] for string in abs ]
print(strx)

