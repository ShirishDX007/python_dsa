#write Bubble sort alorithm

def bubble_sort_list(lst):
    #traverse through all list numbers
    for i in range(len(lst)):
        for j in range(0, len(lst) -i -1 ):
            #travers the list from 0 to size of lst - i-1
            #swap the numbers if found greater than the next number
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

if __name__ == '__main__':
    lst = [3,5,6,2,1,8]
    bubble_sort_list(lst)
    print(lst)
     