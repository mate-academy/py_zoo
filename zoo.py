"""
docstring
"""


class Zoo:
    """
    zoo class
    """
    def __init__(self):
        """
        def animals list
        """
        self.animals = []

    def get_animals(self):
        """

        :return:
        """
        return self.animals

    def add_animals(self, animal):
        """

        :param animal:
        :return:
        """
        self.animals.append(animal)


class Animal:
    """
    animal class
    """
    def __init__(self, name):
        """

        :param name:
        """
        self.name = name
        self.voice = ''

    def get_name(self):
        """

        :return:
        """
        return self.name

    def get_voice(self):
        """

        :return:
        """
        return self.voice


class Dog(Animal):
    """
    dog class
    """
    def __init__(self, name):
        """

        :param name:
        """
        super().__init__(name)
        self.voice = 'woof'

    def say(self):
        """

        :return:
        """
        return self.voice


class Cat(Animal):
    """
    cat class
    """
    def __init__(self, name):
        """

        :param name:
        """
        super().__init__(name)
        self.voice = 'meow'

    def say(self):
        """

        :return:
        """
        return self.voice


class Bird(Animal):
    """
    bird class
    """
    def __init__(self, name):
        """

        :param name:
        """
        super().__init__(name)
        self.voice = 'tweet'

    def say(self):
        """

        :return:
        """
        return self.voice
