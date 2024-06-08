#write Bubble sort alorithm

def bubble_sort_list(lst):
    #traverse through all list numbers
    for i in range(len(lst)):
        for j in range(0, len(lst) -i -1 ):
            #travers the list from 0 to size of lst - i-1
            #swap the numbers if found greater than the next number
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                
def selection_sort(lst):
    for i in range(len(lst)):
        min_index = i
        for j in range(i + 1, len(lst)):
            if lst[min_index] > lst[j]:
                min_index = j
        
        lst[i], lst[min_index] = lst[min_index] , lst[i]


if __name__ == '__main__':
    lst = [3,5,6,2,1,8]
    bubble_sort_list(lst)
    selection_sort(lst)
    print("Bubble sort:" , lst)
    print("_"*100)
    print("Selection sort:" , lst)
     