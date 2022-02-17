"""
## 2-reading_number.py
Write a function that outputs the transcription of an input number with two digits.

Example:

28---------------->Twenty Eight
"""
def to_text():
    """ This function outputs the transcription of an input number with two digits. """

    unit_digits = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    tens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "ninteen"]
    tens_digits = ["", "ten", "twenty", "thirty", "fourty", "fifty", "sixty", "seventy", "eighty", "ninty"]

    num = input("Please type a two-digit number: ") # get a two-digit number from user

    if int(num[0]) == 1: # numbers from 10 to 19 have a special name. So we have show them for their one part special name
        print(tens[int(num[1])])

    else: # but the numbers from 20 to 99 not have a special name. So we can display them with to part. First part is first number, second part is second number
        print(tens_digits[int(num[0])], unit_digits[int(num[1])])
        
to_text()