# Author: Brandon Hoffman Date: 10/25/2020 Description: create a function that takes a list of names and stores any
# value that starts with the letter 'K' in a new list concatenated also with the string ' Hoffman'

def add_surname(name_list) -> list[str]:
    """
    takes a list of names and stores any value that starts with the letter 'K' in a new list concatenated also with
    the string ' Hoffman'
    """
    new_name_list: list[str] = []
    for name in name_list:
        if name[0] == 'K':
            new_name_list += [name + ' Hoffman']

    return new_name_list


# testing the function
names: list[str] = ["Kiki", "Krystal", "Pavel", "MaryKay", "Annie", "Koala"]
changed_name_lists: list[str] = add_surname(names)
for name in changed_name_lists:
    print(name)
