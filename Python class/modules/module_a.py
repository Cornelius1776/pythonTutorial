""" When modules are imported in python, the interpreter sets a special variable called __name__
The interpreter set the value of __main__ for the module being imported into, while the name of the
imported module is the value given to __name__"""

import module_b
""" print(__name__) #__main__
print(module_b.__name__) # module_b """

if __name__ == "__main__":
    print("Module run directly")
else:
    print("Module imported")


def add(a, b):
    print(a + b)


add(53, 46)
