import csv

# -------------------------hard way
with open('weather_data.csv') as file:
    data = csv.reader(file)
    temperatures = []
    for row in data:
        if row[1] != 'temp':
            temperatures.append(int(row[1]))
    print(temperatures)
# --------------------------easy way
import numpy as np
import pandas as pd

data = pd.read_csv('weather_data.csv')
# print(data['temp'])
data_dict = data.to_dict()  # saves the data into a dictionary
print(data_dict)

# saves temp column into a list
temp_list = data['temp'].tolist()
print(len(temp_list))
print(temp_list)

# getting data in a column
print(data['temp'].mean())
print(data['temp'].max())

print(data.condition)

# get data in a row
print(data[data.day == 'Monday'])

print(data[data.temp == data.temp.max()])  # grabs the row that had the highest temp in the temp column


def temp_conversion(temp):
    return temp * 1.8 + 32


monday = data[data.day == 'Monday']
print(temp_conversion(monday.temp))

# --------------------------
import pandas as pd
# create a dataframe from scratch
data_dict = {
    'students': ['Amy', 'James', 'Angela'],
    'scores': [76, 56, 65]
}
data = pd.DataFrame(data_dict)
data.to_csv('new_data.csv')
