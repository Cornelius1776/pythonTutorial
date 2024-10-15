# these are ways to manipulate the output of strings

name = "John"
greet = "Hello"
print(f"Cornelius {greet}") # fstring
print(greet, "Dami and", name)
print(f"{greet} {name} nice to meet you." )
print("I love "+"python")

# formatted string (f"") is the preferred syntax
pet_name = "Bold"
pet_age = 7
message = f"{pet_name} is {pet_age} months old"
print(message)

# format() can also be used
message = "Our dog {} is {} months old".format(pet_name, pet_age)
print(message)

# or
message = "Our dog {} is {} months old"
print(message.format(pet_name, pet_age))

# format() supports positional argument. the arguments are indexed from 0
message = "Our dog {0} is {1} months old".format(pet_name, pet_age)
print(message)

# format() also supports keyword argument.
message = "Our dog {pet_name} is {pet_age} weeks old".format(
    pet_name="lily", pet_age=6)
print(message)

# multi-line strings
character_name = "Sam"
story = f"""{character_name} was in his room
when he had a knock on the door, but {character_name} found
nobody, then {character_name} took a shower and went out. """
print(story)


#String indexing
animal = "Lion"
print(animal[0])
print(animal[1])
print(animal[2])
print(animal[3])

print(animal[-1])
print(animal[-2])
print(animal[-3])
print(animal[0])

print(animal[1: 3])