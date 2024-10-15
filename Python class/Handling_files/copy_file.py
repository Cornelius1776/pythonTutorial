import shutil

# copyfile() copies the contents of a file i.e. source to destination. Most efficient way to copy
shutil.copyfile("src.txt", "dst.txt")  # source, destination

# copy() copies file, and the destination may be a directory(folder). returns destination
shutil.copy("src.txt", "dst.txt")

# copy2() copies file alongside its metadata. returns destination
shutil.copy2("src.txt", "dst.txt", )
