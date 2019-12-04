"""Zoo module"""

class Zoo:
    """zoo class, init list with animals"""
    def __init__(self):
        self._animals = []

    def add(self, animal):
        """add animal in zoo list"""
        self._animals.append(animal)

    def get_animals(self):
        """get all zoo list"""
        return self._animals


class Animal:
    """Parent animal class"""
    def __init__(self, name):
        self._name = name
        self._voice = None

    def get_name(self):
        """return animal name"""
        return self._name

    def say(self):
        """return what animal say"""
        return self._voice

class Dog(Animal):
    """behavior dog class"""
    def __init__(self, name):
        super().__init__(name)
        self._voice = "woof"


class Cat(Animal):
    """behavior cat class"""
    def __init__(self, name):
        super().__init__(name)
        self._voice = "meow"


class Bird(Animal):
    """behavior bird class"""
    def __init__(self, name):
        super().__init__(name)
        self._voice = "tweet"
