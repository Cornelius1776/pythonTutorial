import os

source = "test.txt"
destination = "C:\\Users\\USER\\Desktop\\test.txt"

try:
    if os.path.exists(destination):
        print("another file exist at this location")
    else:
        os.replace(source, destination)
        print(f"{source} was moved")

except FileNotFoundError:
    print(f"{source} not found")

# the same goes for moving folders
