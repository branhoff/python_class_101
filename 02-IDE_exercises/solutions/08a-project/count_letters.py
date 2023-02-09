# Author: Brandon Hoffman
# Date: 11/14/2020
# Description: creates a function called count_letters that takes as a parameter a string
#              and returns a dictionary that tabulates how many of each letter is in that string.

def count_letters(string) -> dict[str, int]:
    """
    Input: a string
    Output: a dictionary with the key as a capital letter and the value as the count
            of occurrences of the upper and lower case occurences of that letter
    """

    letter_counts: dict[str, int] = {}

    for c in string:

        if 'A' <= c.upper() <= 'Z':

            if c.upper() not in letter_counts:
                letter_counts[c.upper()] = 1

            else:
                letter_counts[c.upper()] += 1

    return letter_counts


# Testing

word: str = "AaBb"
print(count_letters(word))  # should  print {'A': 2, 'B': 2}
