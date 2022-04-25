import pandas as pd
data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
gray_data = len(data[data['Primary Fur Color'] == 'Gray'])
black_data = len(data[data['Primary Fur Color'] == 'Black'])
cinnamon_data = len(data[data['Primary Fur Color'] == 'Cinnamon'])

data_dict = {
    'Fur Color': ['Gray', 'Black', 'Cinnamon'],
    'Count': [gray_data, black_data, cinnamon_data]
}
squirrel =  pd.DataFrame(data_dict)
squirrel.to_csv('squirrel_count.csv')
print(squirrel)