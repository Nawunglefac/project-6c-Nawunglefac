# Author: Napoleon Awunglefac
# GitHub username: Nawunglefac
# Date: 02/15/2023
# Description: We will write a class that
# contains 2 parameters (a person's name and age). Then we will have a function that calculates the standard
# deviation between the ages of those on the list

class Person:
    def _int_(self, name, age):
        self._name = name
        self._age = age

    def get_age(self):
        return self._age


def std_dev(person_list):
    total = 0
    for person in person_list:
        total += person.get_age()
    mean_age = total / len(person_list)

    squared_sum = 0
    for person in person_list:
        squared_sum += (mean_age - person.get_age()) ** 2

    return (squared_sum / len(person_list)) ** 0.5


p1 = Person("A", 73)
p2 = Person("B", 24)
p3 = Person("C", 48)

person_list = [p1, p2, p3]
answer = std_dev(person_list)
print("standard dev of age:", answer)
