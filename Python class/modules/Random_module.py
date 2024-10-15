import random

# randint() prints random numbers between the specified arguments
x = random.randint(1, 6)
print(x)

# random() prints floats less than 1
y = random.random()
print(y)

# choice choose a random item from a data structure
countries = ["USA", "UK", "Lichenstein", "Luxembourg", "Switzerland"]
favorite = random.choice(countries)
print(favorite)

# shuffle() shuffles up elements in the data
dice = [1, "A", 2, "B", 3, "C", 4, "D", 5, "E", 6, "F"]
random.shuffle(dice)
print(dice)
