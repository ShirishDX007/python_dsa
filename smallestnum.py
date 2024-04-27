x = [35, 20, 15, 9, 45, 10, 50, 75]

#Initialize the smallest number from list as first element
smallest = x[0]

#Iterate through the list from second element
for num in x[1:]:
    if num < smallest:

        smallest = num

print(f"Smallest number from list is", smallest)

print("smallest number using min method..")

smallest_num = min(x)
print(smallest_num)

print("--***--smallest number using sorted method--***--")

sorted_num = sorted(x)
smallest = sorted_num[0]
print(smallest)