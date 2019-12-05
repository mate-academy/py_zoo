"""This program  processes animals behaviour in the zoo"""


class Zoo:
    """This is class for operating with animals"""
    def __init__(self):
        """Set the array of animals"""
        self.animals = []

    def add(self, animal):
        """Add the inhabitants to the zoo"""
        self.animals.append(animal)

    def get_animals(self):
        """Return list of zoo inhabitants"""
        return self.animals


class Animal:
    """This is parent class for all zoo animals"""
    def __init__(self, name, say):
        """Initiate basic class variables"""
        self.name = name
        self.say_s = say

    def get_name(self):
        """Return name from class object"""
        return self.name

    def say(self):
        """Refer to the sound of animal"""
        return self.say_s


class Dog(Animal):
    """This is child class for type of animals"""
    def __init__(self, name, say="woof"):
        """Re-assign sound of child class"""
        super().__init__(name, say)


class Cat(Animal):
    """This is child class for type of animals"""
    def __init__(self, name, say="meow"):
        """Re-assign sound of child class"""
        super().__init__(name, say)


class Bird(Animal):
    """This is child class for type of animals"""
    def __init__(self, name, say="tweet"):
        """Re-assign sound of child class"""
        super().__init__(name, say)
