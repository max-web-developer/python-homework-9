# нужно поменять местами первый и последный член словаря:

from abc import abstractproperty


def change(lst):
    new_start = lst.pop() 
    new_end = lst.pop(0)  
    lst.append(new_end)  
    lst.insert(0, new_start)  
    new_end=['new_key']
    new_end.append(lst)
    return lst
print(change(lst=[1,2,3,4,5]))