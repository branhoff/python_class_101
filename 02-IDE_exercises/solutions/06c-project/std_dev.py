# Author: Brandon Hoffman
# Date: 10/25/2020
# Description: Creates a Person class to initialize a name and age.
#              Then creates a std_dev function that can take a list of person
#              objects and calculate a standard deviation on the age

class Person:
    """
    Represents a person
    """

    def __init__(self, name, age) -> None:
        """
        Intializes a person's name and age
        """
        self._name = name
        self._age = age

    def get_age(self) -> int:
        """
        returns the age of a person object
        """
        return self._age


def std_dev(person_list) -> float:
    """
    Takes in a list of 'Person' objects and returns the standard deviation of their ages
    """
    age_sum = 0
    for person in person_list:
        age_sum += person.get_age()

    avg = age_sum / len(person_list)

    variance = 0
    for person in person_list:
        variance += (person.get_age() - avg) ** 2

    stdv = (variance / len(person_list)) ** 0.5

    return stdv


person1 = Person("Katie", 73)
person2 = Person("Tran", 24)
person3 = Person("Hanna", 48)
person_list: list[Person] = [person1, person2, person3]
print(std_dev(person_list))
