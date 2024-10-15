# A higher order function is a function that 1. return function, or 2. takes function as argument

# returns a function in this case the built-in function upper()
def greet(message):
    return message.upper()


# accepts a function as argument
def hey(fun):
    message = fun("Hey")
    print(message)


print(greet("Hello"))
hey(greet)


# add() returns inner_add()
""" def add(x):
    def inner_add(y):
        print(x + y)
    return inner_add(3)


add(3) """


# or this syntax
""" def add(x):
    def inner_add(y):
        print(x + y)
    return inner_add


my_add = add(1)
my_add(1) """


# or this
def add(x):
    def inner_add(y):
        return x + y
    return inner_add


my_add = add(3)
print(my_add(2))

# built-in methods sort(), map(), filter() etc examples of higher order functions
