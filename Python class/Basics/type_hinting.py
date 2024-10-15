# Even though python is a dynamically typed language, it is not a good idea to
# reassign a variable of one type to the value of another type.

name = "Tom"
print(name)

# name = 3
# print(name)

# Type hint syntax (:type) helps to make sure this can not happen or simply go to vscode settings
# search and enable mypy, although we will still get the output, because python is a dynamically
# typed language. However, red lines will be displayed on the code to tell that something is
# not right.

city: str = "New York"
print(city)

city = "Nashville"
print(city)

# city = 32 #Error message
# print(city)

price: int = 1
print(price)

price = 2
print(price)

# price = 2.2 # Error
# print(price)

# price = "wrong" # Error
# print(price)

rate: float = 1.2
print(rate)

rate = 32.3
print(rate)

rate = 2  # Works fine because the float type can store int type as a literal
print(rate)
