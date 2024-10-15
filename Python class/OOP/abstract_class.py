# abstract method is a method with declaration but no implementation. A class containing abstract
# methods is called an abstract class. the implementation of the methods can be done in the derived
# classes, this will prevent creating any useful objects based on the abstract class.
# abc needs to be imported. abc means abstract base class
# However, all the methods declared as abstract in the abstract class MUST be overridden in the derived
# classes, else error will occur.

from abc import ABC, abstractmethod


class Animal(ABC):  # abstract class
    @abstractmethod
    def eat(self):
        pass


class Carnivore(Animal):
    def eat(self):
        print("This animal eats flesh")


class Herbivore(Animal):
    def eat(self):
        print("This animal eats vegetation")


# a_1 = Animal() This becomes error after importing abc and abstractmethod
c_1 = Carnivore()
h_1 = Herbivore()

# a_1.eat()
c_1.eat()
h_1.eat()
