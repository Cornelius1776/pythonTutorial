# When the name of the methods in a derived class is the same as that of the base class, the method of
# the derived class will override that of the base class
class Vehicle:
    def wheel(self):
        print("This vehicle has a certain number of wheels")

    def turn_on(self):
        print("Turn on the vehicle")

    def move(self):
        print("The vehicle is moving")


# Wheel() will be overriden in the derived classes.
# Derived class objects will call the other methods from Vehicle, but wheel will be overriden and
# called from the respective derived classes
class Car(Vehicle):
    def wheel(self):
        print("cars have four wheels")
    pass


benz = Car()
benz.wheel()
benz.turn_on()
benz.move()


class Bike(Vehicle):
    def wheel(self):
        print("Bikes have two wheels")


suzuki = Bike()
suzuki.turn_on()
suzuki.move()
suzuki.wheel()
