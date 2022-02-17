"""
## 4-unique_list.py
Write a function that filters all the unique(unrepeated) elements of a given list.
Example:
Function call: unique_list([1,2,3,3,3,3,4,5,5])
Output       : [1, 2, 3, 4, 5]
"""

def make_uniq():
    """ This function that takes a list and returns a new list with unique elements of the first list. """
    lst = [1,2,3,3,3,3,4,5,5] # input list
    new_lst = set(lst) # convert list to set
    lst = list(new_lst) # convert set to list
    return lst #return the last form of the list (with no repetition)
print(make_uniq())