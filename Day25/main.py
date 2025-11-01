import csv
import pandas as pd

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

data = pd.read_csv("weather_data.csv")
data_dict = data.to_dict()
temp_list = data["temp"].to_list()

# for getting a single row: 
# eg: data[data.day == "Monday"] -> gives the row for which the day is a monday
print(data[data.day == "Monday"])

# data[data.temp == data.temp.max()] -> gives the row for which the temperature is the maximum


# create a dataframe scratch
my_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [78, 45, 56]
}

second_data = pd.DataFrame(my_dict)
second_data.to_csv("new_data.csv")
