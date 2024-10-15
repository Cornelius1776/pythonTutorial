# This is an important syntax that makes programming interactive
user_name = input("What is your name? ")
print(f"Hello {user_name}")

# All inputs are of string type, so if you intend to input a different type, it has to be type
# cast like age and height below

age = int(input("How old are you? "))
age += 1
print(f"{user_name} will be {age} years old")

height = float(input("How tall are you (in feets)? "))
print(f"You are {height} fts tall.")

favorites = bool(input("Do you like technology?"))
