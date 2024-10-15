# args is a parameter that enables a function to take varying amount of arguments args is a tuple

""" def multiply(x, y, z):
    return x * y * z


print(multiply(2, 98)) Error
 """


def add(*args):  # Could be a name other than args, * is the important syntax
    total_sum = 0
    for i in args:
        total_sum = total_sum + i
    return total_sum


print(add(2, 4, 5, 6))

class Person:
    name