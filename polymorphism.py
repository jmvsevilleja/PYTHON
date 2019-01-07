# Polymorphism is an important feature of class definition in Python
# that is utilized when you have commonly named methods across classes or subclasses


class Shark():
    def swim(self):
        print("The shark is swimming.")

    def swim_backwards(self):
        print("The shark cannot swim backwards, but can sink backwards.")

    def skeleton(self):
        print("The shark's skeleton is made of cartilage.")


class Clownfish():
    def swim(self):
        print("The clownfish is swimming.")

    def swim_backwards(self):
        print("The clownfish can swim backwards.")

    def skeleton(self):
        print("The clownfish's skeleton is made of bone.")


sammy = Shark()
sammy.skeleton()

casey = Clownfish()
casey.skeleton()
sammy = Shark()
sammy.skeleton()

casey = Clownfish()
casey.skeleton()

print("---")
sammy = Shark()

casey = Clownfish()

for fish in (sammy, casey):
    fish.swim()
    fish.swim_backwards()
    fish.skeleton()


def in_the_pacific(fish):
    fish.swim()


print("---")
sammy = Shark()

casey = Clownfish()

in_the_pacific(sammy)
in_the_pacific(casey)
