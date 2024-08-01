def remove_duplicates_inplace(lst):
    #remove duplicates in list inplace without creating new list
    lst[:] = [x for x in lst if not lst.count(x)>1]
    return lst

lst = [1,2,3,4,2,4,5]
print(id(lst))
print(remove_duplicates_inplace(lst))
print(id(lst))

"""  #Shallow copy and deep copy
        >>> import copy
        >>> sh_lst = copy.copy(lst)
        >>> print(id(sh_lst))
        2663381905472
        >>> print(id(lst))
        2663381955392
        >>> dp_lst = copy.deepcopy(lst)
        >>> print(id(dp_lst))
        2663381905216
        >>> lst.append(6)
        >>> lst
        [1, 2, 3, 4, 2, 4, 5, 6]
        >>> print(id(dp_lst))
        2663381905216
        >>> sh_lst = copy.copy(lst)
        >>> print(id(sh_lst))       
        2663381904384
        >>> print(id(lst))    
        2663381955392
        >>> lst.remove(4)
"""