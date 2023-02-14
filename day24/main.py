# file = open("a.txt")
# file = open("C:\\Users\\Edson\\Documents\\GitHub\\pythontraining\\day24\\a.txt")
# content = file.read()
# print(content)
# file.close()

# with open("C:\\Users\\Edson\\Documents\\GitHub\\pythontraining\\day24\\a.txt") as file:
#     contents = file.read()
#     print(contents)

with open("C:\\Users\\Edson\\Documents\\GitHub\\pythontraining\\day24\\new.txt", mode="w") as file:
    file.write("\nEita nóiss.")
    # print(contents)
