heights_in_feet = {"Messi": 5, "Shaq": 7, "Usain": 7, "Ronaldo": 6}

heights_in_metre = {key: (value * 0.3048)
                    for (key, value) in heights_in_feet.items()}
print(heights_in_metre)


def stature(value):
    if value > 2:
        return "Giant"
    elif value > 1.8 and value <= 2:
        return "Tall"
    else:
        return "average"


heights_in_metre = {key: stature(value * 0.3048)
                    for (key, value) in heights_in_feet.items()}

print(heights_in_metre)
