#write Bubble sort alorithm
#write pseudocode for bubble sort algorithm
 #1. Iterate through the list from the first element to the last element.
 #2. For each element, compare it with the next element in the list.
 #3. If the current element is greater than the next element, swap them.
 #4. Repeat steps 2 and 3 until the end of the list is reached.
 #5. Repeat steps 1 to 4 until the list is sorted.



def bubble_sort_list(lst):
    #traverse through all list numbers
    for i in range(len(lst)):
        for j in range(0, len(lst) -i -1 ):
            #travers the list from 0 to size of lst - i-1
            #swap the numbers if found greater than the next number
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

#write pseudocode for selection sort algorithm
#1.iterate through the list from  first to last element
#2.Find the minimum element in the sorted list
#3.Swap the found minimum element with first element
#4.repeat the steps 2 and steps 3 until the list is sorted


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
     