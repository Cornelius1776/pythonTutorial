# file in the same directory
with open("src.txt") as file:
    print(file.read())

print(file.closed)

# file from an external directory

with open("C:\\Users\\USER\\Desktop\\JavaScript\\variables.js") as file:
    print(file.read())


# To handle a file not found using exception handling
try:
    with open("C:\\Users\\USER\\Desktop\\JavaScript\\variables.j") as file:
        print(file.read())
except FileNotFoundError as error:
    print(error)
    print("enter existing paths only")
except Exception:
    print("Something's wrong")
