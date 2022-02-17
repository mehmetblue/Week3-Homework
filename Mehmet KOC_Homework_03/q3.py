"""
## 3-alphabetical_order.py
Write a function that takes an input of different words with hyphen (-) in between them and then:

sorts the words in alphabetical order,
adds hyphen icon (-) between them,
gives the output of the sorted words.

Example:
Input  >>> green-red-yellow-black-white
Output >>> black-green-red-white-yellow 

"""
def to_sort():
    """ This function takes an input of different words with hyphen (-) in between them and then:

    sorts the words in alphabetical order,
    adds hyphen icon (-) between them,
    gives the output of the sorted words. """

    words = input("Please type the words: ") # get words from user
    words_list = words.split("-") # split the words from the hyphens(-)
    words_list.sort() # sorted ascending

    print("-".join(words_list)) # join the words wit hyphens(-) and display

to_sort()