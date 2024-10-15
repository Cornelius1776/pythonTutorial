# List is also known as arrays in some other programming languages, it is a data structure
# that acts like a variable that stores multiple values in Python, but it is a whole different
# animal in C/C++

fruits = ["paw paw", "cucumber", "orange", "apple", "banana"]
print(fruits)

# for loop can easily be used to print each of the element in the array individually.
for fruit in fruits:
    print(fruit)

# elements can be accessed using their index number, starting at 0
print(fruits[1])

mixture = ["Hi", 23, 3.14159, True]
print(mixture)
print(mixture[2])

for fruit in fruits:
    print(f"I love {fruit}.")

# List methods
count = len(fruits)  # len() gives the number of element in the list
print(count)

removed_fruit = fruits.pop()  # removes the last element of the list
print(fruits)
print(f"{removed_fruit} has been removed.")

fruits.append("watermelon")  # adds element to the end of the list
print(fruits)

fruits.reverse()  # rearranges the element
print(fruits)

fruits.remove("cucumber")  # removes a particular element
print(fruits)

# adds an element at any position in the list using the index location
fruits.insert(1, "cucumber")
print(fruits)

fruits.remove("paw paw")

if "paw paw" in fruits:
    print("Let's eat paw paw")
else:
    print("We need to buy from the market")

fruits.sort()  # rearranges the elements in ascending order
print(fruits)

# pop() method can also be used to remove specific elements using their index
fruits.pop(2)
print(fruits)

# Multi-Dimensional list this is a list that contains another list
mammals = ["rat", "cat", "dog", "bat"]
carnivores = ["lion", "sharks", "crocodiles", "tiger"]
fishes = ["eel", "salmon", "cod", "puffer fish"]
birds = ["owl", "Eagle", "flamingo", "albatross"]

# animal is a 2D list
animals = [mammals, carnivores, fishes, birds]
print(animals)

# accessing the elements in 2D array is the same as a normal array
print(animals[3])
print(animals[0][2])
print(animals[1][0])
print(animals[1][3])

carnivores.pop(2)
print(animals[1])

print(mixture)
mixture.clear()
print(mixture)

names = list("Jon")
print(names)

