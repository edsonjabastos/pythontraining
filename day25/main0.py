import pandas
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

dss = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# dss[dss['Primary Fur Color'] == "Cinnamon"]
print(dss[dss["Primary Fur Color"] == "Cinnamon"].shape[0])
print(dss[dss["Primary Fur Color"] == "Black"].shape[0])
print(dss[dss["Primary Fur Color"] == "Gray"].shape[0])

scd = {
    "color": ["gray", "black", "red"],
    "count": [
        dss[dss["Primary Fur Color"] == "Gray"].shape[0],
        dss[dss["Primary Fur Color"] == "Black"].shape[0],
        dss[dss["Primary Fur Color"] == "Cinnamon"].shape[0],
    ],
}

scdf = pandas.DataFrame(scd)
scdf.to_csv("scdf.csv")