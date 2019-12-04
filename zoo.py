"""There are three kinds of animals in a zoo. """


class Zoo:
    """implementation zoo object"""
    def __init__(self):
        self.animals = []

    def get_animals(self):
        """return all animals in zoo"""
        return self.animals

    def add(self, animal):
        """add new animal in zoo"""
        self.animals.append(animal)


class Animal:
    """animal object"""
    def __init__(self, name):
        self.name = name
        self.word = ""

    def get_name(self):
        """return name animal"""
        return self.name

    def say(self):
        """return word """
        return self.word


class Dog(Animal):
    """dog implementation"""
    def __init__(self, name):
        super().__init__(name)
        self.word = "woof"


class Cat(Animal):
    """cat implementation"""
    def __init__(self, name):
        super().__init__(name)
        self.word = "meow"


class Bird(Animal):
    """bird implementation"""
    def __init__(self, name):
        super().__init__(name)
        self.word = "tweet"
