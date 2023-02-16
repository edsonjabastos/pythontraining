import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open("file1.txt") as file1:
    f1_arr = file1.readlines()
    # f1_arr = [n.strip() for n in f1_arr]
print(f1_arr)
with open("file2.txt") as file2:
    f2_arr = file2.readlines()
    # f2_arr = [n.strip() for n in f2_arr]
print(f2_arr)

se_tem = [int(n) for n in f1_arr if n in f2_arr]

print(se_tem)
