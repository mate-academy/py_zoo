"""
module zoo with animals
"""


class Animal:
    """
    Class using for creation an instance of Animal
    """

    def __init__(self, name):
        self._name = name
        self._voice = 'Hi, I\'m an animal'

    def get_name(self):
        """
        Return the name of animal.
        :return: str
        """
        return self._name

    def say(self):
        """
        Return the voice of animal.
        :return: str
        """
        return self._voice


class Dog(Animal):
    """
    Class using for creation an instance of Dog.
    Inherits from Animal class.
    """

    def __init__(self, name):
        super().__init__(name)
        self._voice = 'woof'


class Cat(Animal):
    """
    Class using for creation an instance of Cat.
    Inherits from Animal class.
    """

    def __init__(self, name):
        super().__init__(name)
        self._voice = "meow"


class Bird(Animal):
    """
    Class using for creation an instance of Bird.
    Inherits from Animal class.
    """

    def __init__(self, name):
        super().__init__(name)
        self._voice = "tweet"


class Zoo:
    """
    Class using for creation an instance of Zoo.
    Using for keeping information about Animal instances.
    """

    def __init__(self):
        self._animals = []

    def get_animals(self):
        """Return the list of animals of zoo.
        :return: list
        """
        return self._animals

    def add(self, animal):
        """
        Add animal to zoo.
        :param animal:
        :return: None
        """
        self._animals.append(animal)
