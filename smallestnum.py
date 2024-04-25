x = [35, 20, 15, 99, 45, 10, 50, 75]

#Initialize the smallest number from list as first element
smallest = x[0]

#Iterate through the list from second element
for num in x[1:]:
    if num < smallest:

        smallest = num

print(f"Smallest number from list is", smallest)