# keyword argument enables parameter to be matched with an argument regardless of the arrangment
# when calling the function


def message(first_name, last_name, age):
    return f"{first_name} {last_name} is {age} years old."


print(message("John", "Doe", 25))
print(message(25, "Doe", "John"))  # not good
print(message(age=25, last_name="Doe", first_name="John"))  # keyword argument
