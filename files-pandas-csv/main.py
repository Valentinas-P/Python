
#----------------------------------CSV----------------------------------------------------

# with open("weather_data.csv") as file:
#     data = file.readlines()
#     print(data)
#
# import csv
#
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     print(data)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)


# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)


# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     next(data)
#     for row in data:
#         temperatures.append(int(row[1]))
#     print(temperatures)
# #
# #
# #
# with open("weather_data.csv") as data_file2:
#     data = csv.reader(data_file2)
#     temperatures2 = []
#     for each_row in data:
#         if each_row[1] != "temp":
#             temperatures2.append(int(each_row[1]))
#     print(temperatures2)

# ----------------------------------PANDAS LIB----------------------------------------------------

# import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])

# temp_list = data["temp"].to_list()
# print(temp_list)
# #Finding average in temp
# average = sum(temp_list) / len(temp_list)
# print(int(average))
#
# #Finding a mean  and max number in temp
# print(data["temp"].mean())
# print(data["temp"].max())
# #Different way of finding max
# print(data.temp.max())
#
# #Get data in column
# print(data["condition"])
# print(data.condition)

# #Get data in row
# print(data[data.day == "Monday"])
#
# #Find the biggest temp in the column
# print(data[data.temp == max(data.temp)])

#
# #Finding monday temp and converting to fahrenheit
# monday = data[data.day == "Monday"]
# monday_temp_f = (monday.temp * 9/5) + 32
# print(monday_temp_f)

# #Create a dataframe from scratch
# #Example of dict
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# dataa = pandas.DataFrame(data_dict)
# dataa.to_csv("new_data.csv")

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
temp_list = data["Primary_Fur_Color"].to_list()
calculate_grey = temp_list.count("Gray")
calculate_red = temp_list.count("Cinnamon")
calculate_black = temp_list.count("Black")

#Creating a new dataframe from given results
data_dict = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [calculate_grey, calculate_red, calculate_black],
}
datas = pandas.DataFrame(data_dict)
datas.to_csv("squirrel_count.csv")

















