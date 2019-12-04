"""
Module defines zoo and animals that live in it.
Classes
-------
Zoo
Dog(Zoo)
Cat(Zoo)
Bird(Zoo)
"""


class Zoo:
    """
    A class representing a zoo.
    Attributes
    ----------
    _name -- name of the animal or zoo
    _animals -- list af animal objects
    Methods
    -------
    get_name()
    add()
    get_animals()
    """

    def __init__(self, name='Not named'):
        self._name = name
        self._animals = []

    def get_name(self):
        """Return name of the animal or the zoo"""
        return self._name

    def add(self, animal):
        """Add new animal object to the list of animals"""
        self._animals.append(animal)

    def get_animals(self):
        """Return list of animal objects"""
        return self._animals


class Dog(Zoo):
    """
    A class used to represent a dog
    Methods
    -------
    say()
    """

    @staticmethod
    def say():
        """Return sound (str) that the dog makes"""
        return 'woof'


class Cat(Zoo):
    """
    A class used to represent a cat
    Methods
    -------
    say()
    """

    @staticmethod
    def say():
        """Return sound (str) that the cat makes"""
        return 'meow'


class Bird(Zoo):
    """
    A class used to represent a bird
    Methods
    -------
    say()
    """

    @staticmethod
    def say():
        """Return sound (str) that the bird makes"""
        return 'tweet'
