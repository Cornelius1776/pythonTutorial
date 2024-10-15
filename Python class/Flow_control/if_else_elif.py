'''voter_name = input("What is your name? ")
voter_age = int(input(f"Hi {voter_name}, what is your age? "))
message_1: str = f"Congratulations {voter_name}, you are eligible to vote"
message_2: str = f"Sorry {voter_name}, you are NOT eligible to vote"
message_3: str = "Sorry " + voter_name + " you are too old"
message_4: str = f"Hi {voter_name}, stay at home if you want"

if voter_age < 18:
    print(message_2)
elif voter_age > 80:
    print(message_4)
elif voter_age > 90:
    print(message_3)
else:
    print(message_1)
'''

age = int(input("Enter your age: "))
'''
if age > 18:
    if age % 2 == 0:
        print("You are an adult and your age is an even number")
    else:
        print("You are an adult and your age is an odd number")
else:
    print("You are not an adult")
'''

if age > 18 and age % 2 == 0:
    print("You are an adult and your age is an even number")
elif age < 18:
    print("You are not an adult")
else:
    print("You are an adult and your age is an odd number")