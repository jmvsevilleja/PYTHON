class Person(object):
    def __init__(self, name):
        self.name = name

    def reveal_identify(self):
        print("...And I am {}".format(self.name))


class SuperHero(Person):
    def __init__(self, name, hero_name):
        super(SuperHero, self).__init__(name)
        self.hero_name = hero_name

    def reveal_identify(self):
        super(SuperHero, self).reveal_identify()
        print("...And I am super {}".format(self.hero_name))


name = SuperHero('Jess', 'Millionare')
name.reveal_identify()
