from collections import Counter
from itertools import groupby
import random
import names


class Person:
    def __init__(self, eye_color, hair_color, glasses, name):
        self.eye_color = eye_color
        self.hair_color = hair_color
        self.name = name
        self.glasses = glasses

    def number_of_vowels(self):
        counted = Counter(self.name.lower())
        return sum(counted[v] for v in "aeiouy")

    def at_least_one_consecutive(self):
        return max(len(list(v)) for _, v in groupby(self.name.lower())) > 1

    def check_hair(self):
        return self.hair_color

    def check_eyes(self):
        return self.eye_color

    def check_glasses(self):
        return self.glasses

    def ask_name(self):
        return self.name

    def __repr__(self):
        return f"Person(eye_color={self.eye_color}, hair_color={self.hair_color}, glasses={self.glasses}, name={self.name})"


def _person_check(person):
    if person.check_eyes() == "green":
        if person.check_hair() == "red":
            if not person.at_least_one_consecutive():
                return False
        if person.check_glasses():
            if person.number_of_vowels() != 2:
                return False
        else:
            if person.number_of_vowels() != 3:
                return False
        return True
    return False


def _generate_person():
    eye_color = random.choices(['brown', 'blue', 'hazel', 'amber', 'gray', 'green'], weights=[70, 10, 5, 5, 3, 7])[0]
    hair_color = random.choices(['brown', 'blue', 'black', 'red', 'blond', 'green'], weights=[50, 10, 20, 5, 8, 7])[0]
    glasses = random.random() > .6
    person = Person(eye_color=eye_color, hair_color=hair_color, glasses=glasses, name=names.get_first_name())
    return person


def _generate_crowd(size=1000):
    crowd = [Person(eye_color='green', hair_color="black", glasses=False, name="Adila")]
    for _ in range(size):
        p = _generate_person()
        if not _person_check(p):
            crowd.append(p)
    random.shuffle(crowd)
    return crowd


crowd = _generate_crowd()
