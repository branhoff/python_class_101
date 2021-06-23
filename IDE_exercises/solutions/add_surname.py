# Author: Brandon Hoffman
# Date: 10/25/2020
# Description: create a function that takes a list of names and stores any value that starts with the letter 'K' in a new list concatenated also with the string ' Hoffman'

def add_surname(name_list):
    """
    takes a list of names and stores any value that starts with the letter 'K' in a new list concatenated also with the string ' Hoffman'
    """
    return [name + " Hoffman" for name in name_list if name[0] == "K"]