import os

path = "C:\\Users\\USER\\Desktop\\Programming books"

# exists() checks if the path exists
if os.path.exists(path):
    print("path exist")
    if os.path.isfile(path):
        print("path leads to a file")
    elif os.path.isdir(path):
        print("path leads to a directory")
else:
    print("path does not exist")
