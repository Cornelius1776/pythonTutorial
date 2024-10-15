import os

path = "dst.txt"
os.remove(path)

try:
    os.remove(path)
    print("file deleted")
except FileNotFoundError:
    print(f"{path} not found")

# I have never run this piece of code because it will delete the dst.txt.
# To delete directories(folders), shutil should be imported and shutil.rmtree() will be used, and it
# deletes the folder in its entirety. However, empty folder cannot be deleted this way. To delete
# empty folders, os.rmdir() can be used even without importing shutil.
