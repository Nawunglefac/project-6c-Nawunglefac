# Author: Napoleon Awunglefac
# GitHub username: Nawunglefac
# Date: 02/15/2023
# Description: We will write a class that
# contains 2 parameters (a person's name and age). Then we will have a function that calculates the standard
# deviation between the ages of those on the list


class Person:
    """Represents a person with a name and age."""

    def __init__(self, name, age):
        """Creates a new Person with the specified name and age."""
        self._name = name
        self._age = age

    def get_age(self):
        """Returns the age of a Person."""
        return self._age

def std_dev(person_list):
    """Returns the standard deviation of a list of Persons."""
    sum = 0
    for person in person_list:
        sum += person.get_age()

    mean = sum/len(person_list)

    squared_sum = 0
    for person in person_list:
        squared_sum += (person.get_age() - mean) ** 2

    variance = squared_sum / len(person_list)

    deviation = variance ** 0.5

    return deviation

