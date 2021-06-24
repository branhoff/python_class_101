# Author: Brandon Hoffman
# Date: 11/14/2020
# Description: Takes in two strings and returns a set of common words

def words_in_both(string_1, string_2):
    """
    Input: two strings
    Output: a set of common words between the two strings
    """
    set_1 = set(string_1.lower().split())
    set_2 = set(string_2.lower().split())

    return set_1 & set_2