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


class Animal:
    """class used to represent animal"""
    def __init__(self, name):
        self.name = name
        self.sound = ""

    def get_name(self):
        """return name of animal"""
        return self.name

    def say(self):
        """return sound of animal"""
        return self.sound


class Dog(Animal):
    """A class used to represent dog"""
    def __init__(self, name):
        super().__init__(name)
        self.sound = "woof"


class Cat(Animal):
    """A class used to represent cat"""
    def __init__(self, name):
        super().__init__(name)
        self.sound = "meow"


class Bird(Animal):
    """A class used to represent bird"""
    def __init__(self, name):
        super().__init__(name)
        self.sound = "tweet"
