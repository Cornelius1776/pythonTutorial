# This is a short syntax to create a new list

price = []
for i in range(1, 11 + 1):  # to execute for 11
    price.append(i + i)
print(price)


# using list comprehension
price = [i + i for i in range(1, 11)]
print(price)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_number = list(filter(lambda num: num % 2 == 0, numbers))
print(even_number)


# using list comprehension
even_number = [i for i in numbers if i % 2 == 0]
print(even_number)


# can also be modified like this
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = [i if i % 2 != 0 else "even number" for i in numbers]
print(odd_numbers)
