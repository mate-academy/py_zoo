"""
There are three kinds of animals in a zoo.
All of them have names. Also, dogs say "woof", cats say "meow",
birds say "tweet". Implement classes for all kinds of animals
according to tests.
"""


class Zoo:
    """Class Zoo"""
    def __init__(self):
        self.zoo_lst = []

    def add(self, animal):
        """Add animal to zoo"""
        self.zoo_lst.append(animal)

    def get_animals(self):
        """Get all animals"""
        return self.zoo_lst


class Dog:
    """Class Dog"""
    def __init__(self, name):
        self.name = name

    def get_name(self):
        """Get name animal"""
        return self.name

    @staticmethod
    def say():
        """Animal say"""
        return "woof"


class Cat:
    """Class Cat"""
    def __init__(self, name):
        self.name = name

    def get_name(self):
        """Get name animal"""
        return self.name

    @staticmethod
    def say():
        """Animal say"""
        return "meow"


class Bird:
    """Class Bird"""
    def __init__(self, name):
        self.name = name

    def get_name(self):
        """Get name animal"""
        return self.name

    @staticmethod
    def say():
        """Animal say"""
        return "tweet"
