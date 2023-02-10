# Author: Brandon Hoffman Date: 10/25/2020 Description: create a function that takes a list of names and stores any
# value that starts with the letter 'K' in a new list concatenated also with the string ' Hoffman'

def add_surname(name_list: list[str]) -> list[str]:
    """
    takes a list of names and stores any value that starts with the letter 'K' in a new list concatenated also with
    the string ' Hoffman'
    """
    new_name_list: list[str] = []
    for name_in_list in name_list:
        if name_in_list[0] == 'K':
            new_name_list += [name_in_list + ' Hoffman']

    return new_name_list


# Testing the function
names: list[str] = ["Kiki", "Krystal", "Pavel", "MaryKay", "Annie", "Koala"]
changed_name_lists: list[str] = add_surname(names)
name: str
for name in changed_name_lists:
    print(name)
