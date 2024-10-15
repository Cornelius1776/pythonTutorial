# Duck typing is a concept that places less emphasis on the class, but the methods
# and properties are treated more importantly. All the methods must be available.

class Dog:

    def habitat(self):
        print("Dogs are domestic, but some live in the wild")

    def sound(self):
        print("The dog barks")


class Cat:

    def habitat(self):
        print("Cats are domestic, but some live in the wild")

    def sound(self):
        print("The cat meows")


class Animal:
    def catch(self, Dog):
        Dog.habitat()
        Dog.sound()
        print("A good example of duck typing")


dog = Dog()
cat = Cat()
animal = Animal()

# the methods for dog and cat are called respectively, without worrying regarding the Bear class.
animal.catch(dog)
animal.catch(cat)
