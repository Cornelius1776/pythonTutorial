text = "// Written using python file write"

# "a" Will append the new written data, "w" will delete and completely overwrite the file
with open("C:\\Users\\USER\\Desktop\\JavaScript\\variables.js", "a") as file:
    file.write(text)

with open("src.txt", "w") as file:
    file.write(text)
