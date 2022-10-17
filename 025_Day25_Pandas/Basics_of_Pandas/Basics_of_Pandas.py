# with open("weather_data.csv") as main_file:
#     data = main_file.readlines()
#     print(data)

# # NOTES to get the temp row using csv library vs panda
# import csv
# with open("weather_data.csv") as main_file:
#     data = csv.reader(main_file)
#     temprature = []
#     for row in data:
#         if row[1] != "temp":
#             temprature.append(int(row[1]))
#     print(temprature)

import pandas as pd
data = pd.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict)

temp_list = data["temp"].to_list()
# print(temp_list)
# average of temp:
# x = 0
# for temp in temp_list:
#     x += temp
# avg = x / len(temp_list)
# print(round(avg,2))

# or
# average = sum(temp_list) / len(temp_list)
# print(round(average,2))

# or using panda
# print(data["temp"].mean())

# max of temp
# print(data["temp"].max())

# getting data from coloums
# print(data["condition"])
# print(data.condition)

# getting data form rows
# print(data[data.day == "Monday"])

# getting row which have max temp
# print(data[data.temp == data.temp.max()])

# getting specific row and coloumn
# monday = data[data.day == "Monday"]
# print(monday.condition)
# monday_temp =  int(monday.temp)
# infren = (monday_temp * (9/5)) + 32
# print(infren)


# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Ashish"],
    "scores": [12, 14, 15]
}
new_data = pd.DataFrame(data_dict)
# print(new_data)
# to convert it into csv and write
new_data.to_csv("new_data.csv")
