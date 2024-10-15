import time
# loops execute a task repeatedly until a condition is met
# There are different types, for loop, while loop, do-while loop

# for loop
message = "Hello World!"

for letter in message:
    print(letter)  # prints each letter of message independently.

for i in range(10):
    # counting starts from zero ending at 9, +1 makes it 10.
    print(i + 1, "Happy new year")

# Adding a second argument to range for stoppage point
for i in range(5, 20):  # starts at 5, stops at 19
    print(i + 1, "It's a new year")

# adding a third argument for how much i should increment.
for i in range(1, 30, 2):  # increment by 2
    print(i + 2, "It's going to be a great year")

# import time above for this example
seconds = 60

for second in range(seconds, 0, -1):
    print(second)
    time.sleep(1)

print("Happy new year!")


# while loop
""" 
correct_guess = False
exo_planet = "PROXIMA-B"

while correct_guess is not True:
    guess = input("Guess the exo planet >> ")
    if guess.capitalize() == exo_planet.capitalize():
        print(f"You are right the planet is {exo_planet} ")
        correct_guess = True
    else:
        print(f"Wrong! The planet is not {guess}.")
        print("Try again") """

# Another alternative

exo_planet = "PROXIMA-B"

while True:
    guess = input("Guess the exo planet >> ")
    if guess.capitalize() == exo_planet.capitalize():
        print(f"You are right the planet is {exo_planet} ")
        break
    else:
        print(f"Wrong! The planet is not {guess}.")
        print("Try again")

