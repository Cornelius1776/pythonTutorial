# break This statement is used to terminate a loop

# This will continue to ask for your name until your answer the question.
while True:
    name = input("What is you name?")
    if name != "":
        print(f"Hi, {name}")
        break
    else:
        print("You must tell me your fucking name! Asshole")

# continue This statement skips the specified character
# the numbers will be printed without the -
numbers = "123-456-789"

for number in numbers:
    if number == "-":
        continue
    print(number, end="")

# pass
for i in range(1, 30):
    if i == 10:
        print("Skipped 11")
        pass
    else:
        print(i + 1)
