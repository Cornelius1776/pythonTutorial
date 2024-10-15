# Dictionary is a collection of key/value pairs
country_and_capital = {
    # key    |   value
    "Estonia": "Tallinn",
    "Latvia": "Riga",
    "Australia": "Canberra",
    "Austria": "Vienna",
    "Switzerland": "Bern"
}
print(country_and_capital)

# get() prints the value of the specified key
print(country_and_capital.get("Switzerland"))

# prints only the keys (.keys() is optional)
for country in country_and_capital:
    print(country)

# prints only the values(.values() is needed)
for capital in country_and_capital.values():
    print(capital)

#use the key and value in a flexible manner
for country, capital in country_and_capital.items():
    print(f"{capital} is the capital of {country}.")

country_and_capital["Australia"] = "Perth"  # changes the value
print(
    f"I have changed Australian capital to {country_and_capital['Australia']}")

swiss_capital = country_and_capital.get("Switzerland")
print(swiss_capital)

del country_and_capital["Austria"]  # deletes the key/value
print(country_and_capital)

# Dictionaries can have any datatype as their key, including Tuples
person = {
    24: "age",
    ("John", "Doe"): "Fullname",
    True: "male"
}

print(person)
