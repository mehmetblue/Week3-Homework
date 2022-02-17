"""
## 5-equal_reverse.py
Write a function that controls the given inputs whether they are equal to their reversed order or not.

Example:

Input  >>> madam, tacocat, utrecht 

Output >>> True, True, False
"""

def is_palindrome():
    """ This function check the word if it's palindrome or not. input: str, output: boolean """
    word = input("Please type a word: ") # getting word from user    
    if word == word[::-1]:  # comparing the normal and revered form of the words
        print("Yes")        # if the if statement True display "Yes"
    else:
        print("No")         # if the else statement False display "No"

is_palindrome()