'''
Module zoo
'''


class Zoo:
    '''Class for zoo'''
    def __init__(self):
        self.list_of_animal = []

    def get_animals(self):
        '''
        Return all animals in zoo
        :return:
        '''
        return self.list_of_animal

    def add(self, animal):
        '''
        Add animal in zooo
        :param animal:
        :return:
        '''
        self.list_of_animal.append(animal)


class Animal:
    '''Parrent class'''
    def __init__(self, name):
        self.name = name
        self.voice = ''

    def get_name(self):
        '''
        Retyrn animal name
        :return:
        '''
        return self.name

    def get_say(self):
        '''
        REturn animal voice
        :return:
        '''
        return self.voice


class Dog(Animal):
    """Dog class"""
    def __init__(self, name):
        super().__init__(name)
        self.voice = "woof"


class Cat(Animal):
    '''Cat class'''
    def __init__(self, name):
        super().__init__(name)
        self.voice = "meow"


class Bird(Animal):
    '''Bird class'''
    def __init__(self, name):
        super().__init__(name)
        self.voice = "tweet"
