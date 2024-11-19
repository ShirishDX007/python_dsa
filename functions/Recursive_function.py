#pseudocode for recursive function
#1. define factorial function with num as an argument
#2. create a call stack list
#3. check if num is equal to 1
#4. if num is equal to 1 then print base value reached and return 1
#5. else append the input value to call stack list
#6. print the call stack
#7. return num multiply by factorial of num -1

def factorial(num):
    call_stack=[]
    if num == 1:
        print('base value reached. Num is 1.')
        return 1
    else:
        call_stack.append({'input': num})
        print('call stack: ', call_stack)
        return num * factorial(num -1)

print(f"factorial : ",factorial(5))

    
          
        
