volcano = "mount fuji"

# len() checks the length of a string
print(len(volcano))

# find() checks if a character exists in the string
# prints the index of the character if it exists in the string
print(volcano.find("o"))

# prints negative integer if the character does Not exist in the string
print(volcano.find("a"))

# capitalize() changes the first character of the string to uppercase
print(volcano.capitalize())

# upper() converts the entire string to uppercase
print(volcano.upper())

# lower() converts the entire string to lowercase
print(volcano.lower())

# isdigit() checks if the string is a string of digits
print(volcano.isdigit())  # False

price = "123"
print(price.isdigit())  # True

# isalpha() checks if the string contains only alphabetical characters. Space is a non-alphabet
print(volcano.isalpha())  # False


full_name = "JohnDoe"
print(full_name.isalpha())  # True, because no spaces between the characters

# count() checks the number of times a specific character occurs in a string
print(volcano.count("u"))

# replace() replaces the left-side argument with the right-side argument in the entire string
print(full_name.replace("o", "a"))

# * can be used to multiply the output of a string on the same line
print(volcano * 3)

# slice() helps create a substring by extracting characters with indicated indexes from a string
# indexing syntax
x = volcano[0]
print(x)

# the character of the first index is included the second is not.
y = volcano[0:2]  # or just :2
print(y)

# create a substring of characters starting at index 6
z = volcano[6:]
print(z)

a = volcano[0:4:1]
print(a)
a = volcano[0:4:2]
print(a)
a = volcano[0:4:3]
print(a)

# : with a negative step index, removes the last character of the string
reversed_string = volcano[:-1]
print(reversed_string)

# :: with a negative step index, reverses the character of the entire string
reversed_string = volcano[::-1]
print(reversed_string)

# slice() syntax

# the best way to specify the ending index is to use a negative number
my_slice = slice(6, -2)
print(volcano[my_slice])

name = "cornelius"
print(name)
if name[0].islower():
    name = name.capitalize()

print(name)
