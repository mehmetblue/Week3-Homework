"""
##1-perfect_number.py
Perfect number: Perfect number is a positive integer that is equal to the sum of its proper divisors.

The smallest perfect number is 6, which is the sum of 1, 2, and 3.

Some other perfect numbers are 28(1+2+4+7+14=28), 496 and 8128.

Write a function that finds perfect numbers between 1 and 1000. 
Check perfect numbers between 1 and 1000 and find the sum of the perfect numbers using reduce and filter functions.

"""
def find_perfect_number():
    """ This function finds the perfect numbers between 1 and 1000. input: range, output: list """
    
    from functools import reduce

    min, max = 1, 1000 # min and max values for function to search the perfect numbers

    perfect_nums = [] # empty list to gather the perfect numbers

    for num in range(min, max):         # getting every numbers from the given range
        sum = 0                         # temporary variable for adding the divisors while checking the word if it's perfect number
        for i in range(1, num):         # range from 1 to the checking as a divisor
            if num % i == 0:            # finding the proper divisors
                sum += i                # adding to the temporary variable
        if(sum == num):                 
            perfect_nums.append(num)
    print(f"Sum of the Perfect Numbers Between {min} and {max} is", reduce((lambda x, y : x + y), perfect_nums))
    # first part of the sentence is for informing the user min and max numbers.
    # at the second part we use reduce and lambda functions to reach the sum of list which we gather the perfect numbers
            
find_perfect_number()