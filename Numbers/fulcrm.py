def find_fulcrm(lst):
    
    for i in range(len(lst)):
        if sum(lst[:i]) == sum(lst[i+1:]):
            
            return lst[i] 

lst = [3,7,5,4,6]
#sum of 3 + 7 - 10 and 4 + 6= 10 so number of fulcrm are 2
print(find_fulcrm(lst))