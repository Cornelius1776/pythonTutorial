class Animal:
    alive = True
    moves = True
    m_name = None

    def eat(self):
        print("the animal is eating")

    def run(self):
        print("The animal is running very fast")


# Carnivore class inherits from Animal class using the pass keyword
class Carnivore(Animal):
    def carnivore_eat(self):
        print("This animal eats flesh")
    pass


class Herbivore(Animal):
    def herbivore_eat(self):
        print("This animal eats vegetation")
    pass


class Bird(Animal):
    pass


cow = Herbivore()
cow.eat()
cow.herbivore_eat()

albatross = Bird()
print(albatross.alive)

cheetah = Carnivore()
cheetah.run()


# multi-level inheritance. Derived classes can also have other class(es) derive from them
class Lion(Carnivore):
    def sound(self):
        print("Lions roar!")
    pass


simba = Lion()
simba.eat()
simba.carnivore_eat()
simba.sound()


# multiple inheritance. A derived class can inherit from ,multiple parent classes
class Omnivore(Carnivore, Herbivore):
    pass


dog = Omnivore()
dog.herbivore_eat()
dog.carnivore_eat()
