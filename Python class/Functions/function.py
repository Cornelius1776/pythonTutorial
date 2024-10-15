def greet(name):
    print(f"Hello {name}")


greet("Cornelius")
greet("Steve")
greet("Allisson")


def add(num_1, num_2, num_3):
    print(num_1 + num_2 + num_3)


add(1, 1, 1)

# return statement


def multiply(a, b, c):
    return a * b * c


result = multiply(2, 34, 3)  # or simply print(multiply(...))
print(result)


# If a function is called without (), the memory address of the function is returned

print(multiply)
print(add)

address = multiply
print(address)

address = add
print(address)

# built-in functions can also be assigned to variables although not recommended

cout = print
cout("Hello World")
