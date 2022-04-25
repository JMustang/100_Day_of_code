# import csv
#
# with open('weather_data.csv') as f:
#     data = csv.reader(f)
#     tempetures = []
#     for row in data:
#         if row[1] != "temp":
#             tempetures.append(int(row[1]))
#     print(tempetures)


import pandas as pd
data = pd.read_csv('./weather_data.csv')
#
#
# print(data['temp'].mean())
# print(data['temp'].max())
# print(data[data == 'Monday'])
# print(data[data.temp == data.temp.max()])
# monday = data[data.day == 'Monday']
# print(monday.condition)

data_list = {
    'students': ['Any', 'James', 'Angela'],
    'scores': [76, 56, 65]
}
data = pd.DataFrame(data_list)
data.to_csv('new_data_file.csv')