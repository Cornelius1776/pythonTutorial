# walrus operator is used to assign values to variables in part of a larger expression
# The variable behaves like any other variable

print(name := "Cornelius")
print(f"Hi {name}")

numbers = list()
num_of_element = int(input("How many elements do you want to insert in the array? "))
while len(numbers) < num_of_element:
    even_number = int(input("input an even number >>> "))
    if even_number % 2 != 0:
        print("This is an odd number")
        continue
    numbers.append(even_number)

print(numbers)
