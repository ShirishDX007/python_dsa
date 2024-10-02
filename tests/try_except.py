nums = [5,3,5,6]

try:
    avg = sum(nums)/len(nums)
    print('The average of th list is: ', avg)

except:
    print('cannot compute average -make',
          'sure you enter numbers integers')
finally:
    print("Avg of sum is computed.")
    
          
        
