# Author: Brandon Hoffman
# Date: 11/14/2020
# Description: creates a function called count_letters that takes as a parameter a string
#              and returns a dictionary that tabulates how many of each letter is in that string.

def count_letters(string):
    """
    Input: a string
    Output: a dictionary with the key as a capital letter and the value as the count
            of occurrences of the upper and lower case occurences of that letter
    """ 

    letter_counts = {}

    for c in string:
        
        if 'A' <= c.upper() <= 'Z':

            if c.upper() not in letter_counts:
                letter_counts[c.upper()] = 1

            else:
                letter_counts[c.upper()] += 1
            
    return letter_counts