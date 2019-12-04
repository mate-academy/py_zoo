"""modules"""


class Zoo:
    """A class used to represent zoo"""
    def __init__(self):
        self.animals_list = []

    def add(self, animal):
        """add animal to zoo"""
        self.animals_list.append(animal)

    def get_animals(self):
        """return list of animals present in zoo"""
        return self.animals_list


class Dog:
    """A class used to represent dog"""
    def __init__(self, name):
        self.name = name
        self.sound = "woof"

    def get_name(self):
        """return name of animal"""
        return self.name

    def say(self):
        """return sound of animal"""
        return self.sound


class Cat:
    """A class used to represent cat"""
    def __init__(self, name):
        self.name = name
        self.sound = "meow"

    def get_name(self):
        """return name of animal"""
        return self.name

    def say(self):
        """return sound of animal"""
        return self.sound


class Bird:
    """A class used to represent bird"""
    def __init__(self, name):
        self.name = name
        self.sound = "tweet"

    def get_name(self):
        """return name of animal"""
        return self.name

    def say(self):
        """return sound of animal"""
        return self.sound
