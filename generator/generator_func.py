def greeting():
  print('HI')
  yield 1
  print('how are you?')
  yield 2
  
  yield 3
  print('Are you okay?')


messanger = greeting()
result = (messanger)
print(result)