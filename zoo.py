"""Module describes Zoo class and classes for animals"""


class Zoo:
    """Class of a zoo"""
    def __init__(self):
        self._animals = []

    def add(self, animal):
        """Add animal to zoo"""
        self._animals.append(animal)

    def get_animals(self):
        """Get all animals in a zoo"""
        return self._animals


class Dog:
    """Class of dog"""
    def __init__(self, name):
        self._name = name
        self._say = "woof"

    def get_name(self):
        """Get name of a dog"""
        return self._name

    def say(self):
        """What does a dog say?"""
        return self._say


class Cat:
    """Class of cat"""
    def __init__(self, name):
        self._name = name
        self._say = "meow"

    def get_name(self):
        """Get name of a cat"""
        return self._name

    def say(self):
        """What does a cat say?"""
        return self._say


class Bird:
    """Class of bird"""
    def __init__(self, name):
        self._name = name
        self._say = "tweet"

    def get_name(self):
        """Get name of a bird"""
        return self._name

    def say(self):
        """What does a bird say?"""
        return self._say
