import zoo


def test_names():
    c = zoo.Cat("Tom")
    assert c.get_name() == 'Tom'
    d = zoo.Dog("Bandit")
    assert d.get_name() == "Bandit"
    b = zoo.Bird("Charlie")
    assert b.get_name() == "Charlie"


def test_voices():
    z = zoo.Zoo()
    z.add(zoo.Cat("Tom"))
    z.add(zoo.Dog("Bandit"))
    z.add(zoo.Bird("Charlie"))
    assert [animal.say() for animal in zoo.get_animals()] == ["meow", "woof", "tweet"]