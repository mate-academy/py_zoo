"""
Zoo, Animal, Dog, Cat, Bird
"""


class Zoo:
    """
    zoo
    """
    def __init__(self):
        """
        set animals
        """
        self._animals = []

    def add(self, animal):
        """
        add
        """
        self._animals.append(animal)

    def get_animals(self):
        """
        get_animals
        """
        return self._animals


class Animal:
    """
    animal
    """
    def __init__(self, name):
        """
        set voice
        """
        self._name = name
        self._voice = None

    def get_name(self):
        """
        get_name
        """
        return self._name

    def say(self):
        """
        say
        """
        return self._voice


class Dog(Animal):
    """
    dog
    """
    def __init__(self, name):
        """
        set voice
        """
        super().__init__(name)
        self._voice = 'woof'


class Cat(Animal):
    """
    cat
    """
    def __init__(self, name):
        """
        set voice
        """
        super().__init__(name)
        self._voice = 'meow'


class Bird(Animal):
    """
    bird
    """
    def __init__(self, name):
        """
        set voice
        """
        super().__init__(name)
        self._voice = 'tweet'
