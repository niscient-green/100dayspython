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

# Read in csv
import pandas
data = pandas.read_csv("weather_data.csv")
# print(data["temp"])

# Process data into usable objects
data_dict = data.to_dict()
temp_list = data["temp"].tolist()

# Calculate temperature math
total_temp = sum(temp_list)
average_temp = total_temp / len(temp_list)
# print(average_temp)
# print(data["temp"].mean())
# print(data["temp"].max())

# Get row data
# print(data[data.day == "Monday"])
max_temp = data.temp.max()
# print(data[data.temp == max_temp])
monday = data[data.day == "Monday"]
monday_temp = monday.temp[0]
temp_f = monday_temp * 9 / 5 + 32
print(f"{temp_f}")

# Create dataframe from scratch
friends_dict = {
    "friends": ["Jason", "Mike", "Jon"],
    "nickname": ["bozo", "padre", "jon"]
}
friends_df = pandas.DataFrame(friends_dict)
print(friends_df)
friends_df.to_csv("friends.csv")