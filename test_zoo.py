"""
docstring
"""
import zoo


def test_names():
    """

    :return:
    """
    c = zoo.Cat("Tom")
    assert c.get_name() == 'Tom'
    d = zoo.Dog("Bandit")
    assert d.get_name() == "Bandit"
    b = zoo.Bird("Charlie")
    assert b.get_name() == "Charlie"


def test_voices():
    """

    :return:
    """
    z = zoo.Zoo()
    z.add_animals(zoo.Cat("Tom"))
    z.add_animals(zoo.Dog("Bandit"))
    z.add_animals(zoo.Bird("Charlie"))
    assert [animal.say() for animal in z.get_animals()] == ["meow", "woof", "tweet"]
