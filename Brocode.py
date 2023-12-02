import shutil
import os
note = " Python note\nstarted from august to november 2023"
with open("note.txt",'r') as file:

    shutil.copy("note.txt", "copy.txt")
    shutil.copy("note.txt", "move.txt")
    shutil.copy("note.txt", "move1.txt")

source = "move.txt"
destination = "C:\\Users\\Emmanuel\\Desktop\\CV\\move1.txt"
try:
    if os.path.exists(destination):
        print("File path is not empty")
    else:
        os.replace(source,destination)
except FileNotFoundError:
    print(source + "was not found")

    print(help("module"))