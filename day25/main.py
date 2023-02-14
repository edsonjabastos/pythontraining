import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# with open("weather_data.csv", "r") as f:
#     lines = f.readlines()
#     print(lines)
# for line in lines:
#     print(line)
# import csv

# temperatures = []
# with open("weather_data.csv", "r") as weather_file:
#     data = csv.reader(weather_file)
#     print(data)
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#         print(row)
# print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")

print(data)
print(data["temp"])
print(data.temp)
