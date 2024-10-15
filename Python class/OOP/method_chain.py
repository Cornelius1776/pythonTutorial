# Method chaining enables calling multiple methods sequentially. This works by adding 'return self' to
# the method declaration in the class, and using dot notation to add them.

class Vehicle:
    def wheel(self):
        print("This vehicle has a certain number of wheels")
        return self

    def turn_on(self):
        print("Turn on the vehicle")
        return self

    def move(self):
        print("The vehicle is moving")
        return self


car = Vehicle()
car.move().turn_on().wheel()

# \ can be used to split the method calls, this can enable readability.
car.wheel()\
    .turn_on()\
    .move()
