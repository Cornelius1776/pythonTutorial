age = 26
name = 'Cornelius'
print(name)
print(age)

# Variables can be reassigned as many times as we want
name = 'Dami'
age = 28
print(name, age)
print(age)

# multiple assignment can also be done for individual datatypes, or all combined.
# Individual types
Apple, Barclays, Tencent, Samsung = "USA", "UK", "China", "South Korea"
print(Apple)
print(Barclays)
print(Tencent)
print(Samsung)

# Different types combined
fruit, price, weight, life_is_sweet = "Apple", 150, 105.9, True
print(fruit)
print(price)
print(weight)
print(life_is_sweet)

# chained assignment
Yangtze = Thames = Niger = Amazon = "River"  # they all hold the value 'River'
print(Yangtze)
print(Thames)
print(Amazon)
print(Niger)

x = 4
y = 5
z = x + y
print(z)

z = x * y
print(z)

z = y - x
print(z)

a = 17
b = 2
print(a, end=' ')
print(b)
print(a // b)

c = a
print('The memory address of a is', id(a))
print('The memory address of b is', id(b))
print('The memory address of c is', id(c))

print(f'{a + b = } ')
