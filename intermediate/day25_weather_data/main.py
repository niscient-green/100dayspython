# Read and collate weather data

# # Open file, get data - CLUMSY WAY
# with open("weather_data.csv", mode="r") as weather_file:
#     weather_data = weather_file.readlines()
#     weather_file.close()
#     print(weather_data)

# import csv
# with open("weather_data.csv", mode="r") as weather_file:
#     weather_data = csv.reader(weather_file)
#     temperatures = []
#     for row in weather_data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas
data = pandas.read_csv("weather_data.csv")
print(data["temp"])
