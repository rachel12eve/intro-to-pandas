# import csv
#
# with open("weather_data.csv") as data_file:
#     data=csv.reader(data_file)
#     temperatures=[]
#     for row in data:
#         if row[1]!="temp": #remove the first one
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

fur = data["Primary Fur Color"]
# print(fur)

grey = len(fur[fur == "Gray"])
red = len(fur[fur == "Cinnamon"])
black = len(fur[fur == "Black"])
fur_summary = {"Color": ["Gray", "Cinnamon", "Black"],
               "Count": [grey, red, black]
               }

pd.DataFrame(fur_summary).to_csv("Fur Color Count")