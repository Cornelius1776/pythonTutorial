# Tuples are like lists. However, unlike list, they are immutable
europe = ("Estonia", "Ukraine", "Slovenia", "Albania", "Poland", 'Ukraine')
print(f"The European countries are: {europe}.")


for country in europe:
    print(country, end=" ")

print(f"\ncountry at index 2 is {europe[2]}")

asia = ("Sri lanka", "Nepal", "Bhutan", "Myanmar")
print(f"The Asian countries are {asia}")

countries = europe + asia
print(f"The countries combined are {countries}")

if "Valparaiso" in countries:
    print("Really?")
else:
    print("Valparaiso is a city in Chile, not a country")

mixture = ("Hi", 23, 3.14159, True)
print(mixture)

# tuple methods()
print(europe.count("Ukraine"))
print(asia.index("Bhutan"))

repeat = ("London \n") * 10
print(repeat)


