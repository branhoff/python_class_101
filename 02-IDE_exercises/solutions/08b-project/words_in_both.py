# Author: Brandon Hoffman
# Date: 11/14/2020
# Description: Takes in two strings and returns a set of common words

def words_in_both(string_1, string_2) -> set[str]:
    """
    Input: two strings
    Output: a set of common words between the two strings
    """
    set_1: set[str] = set(string_1.lower().split())
    set_2: set[str] = set(string_2.lower().split())

    return set_1 & set_2


# Testing

common_words: str = words_in_both("She's a jack of all trades", 'Jack was tallest of all')
print(common_words)