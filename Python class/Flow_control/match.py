fav_color = input("Enter your favorite color >>").lower()
print(fav_color)

match fav_color:
    case "blue":
        print(f"Your favorite color is {fav_color}.")
    case "gray":
        print(f"Your favorite color is {fav_color}.")
    case "red":
        print(f"Your favorite color is {fav_color}.")
    case "white":
        print(f"Your favorite color is {fav_color}.")
    case "black":
        print(f"Your favorite color is {fav_color}.")
    case _:
        print(f"Your favorite color is not {fav_color}.")
