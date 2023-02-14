from pathlib import Path
print("File      Path:", Path(__file__).absolute())
print("Directory Path:", Path().absolute()) # Directory of current working directory, not __file__ 
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
with open("../a.txt") as file:
    contents = file.read()
    print(contents)
print("File      Path:", Path(__file__).absolute())
print("Directory Path:", Path().absolute()) # Directory of current working directory, not __file__ 
with open("../../.gitignore") as file:
    contents = file.read()
    print(contents)