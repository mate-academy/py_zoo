"""There are three kinds of animals in a zoo. All of them have names.
 Also, dogs say "woof", cats say "meow", birds say "tweet".
 Implement classes for all kinds of animals according to tests."""


class Zoo:
    """Zoo class description"""
    def __init__(self):
        self.animals = []

    def get_animals(self):
        """Returns current list of animals"""
        return self.animals

    def add(self, animal):
        """Add animal to Zoo list"""
        self.animals.append(animal)


class Animal:
    """Class animal description"""

    def __init__(self, name):
        self.name = name
        self.voice = ''

    def get_name(self):
        """Returns name of the animal"""
        return self.name

    def say(self):
        """Returns what animal says"""
        return self.voice


class Dog(Animal):
    """Instance of the Dog class"""

    def __init__(self, name):
        super().__init__(name)
        self.voice = 'woof'


class Cat(Animal):
    """Instance of the Cat class"""

    def __init__(self, name):
        super().__init__(name)
        self.voice = 'meow'


class Bird(Animal):
    """Instance of the Bird class"""

    def __init__(self, name):
        super().__init__(name)
        self.voice = 'tweet'
