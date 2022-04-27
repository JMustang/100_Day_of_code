# import pandas as pd

# my_dict = {'Name': ['Tom', 'Jack', 'Steve', 'Ricky'],
#            'Age': [28, 34, 29, 42],
#            'Rating': [4.23, 3.24, 3.98, 4.31]}

# data = pd.DataFrame(my_dict)
# data.to_csv('new_data_file.csv')
# print(data)


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # new_list = []
# # for n in numbers:
# #     add_1 = n + 1
# #     new_list.append(add_1)
# #
# # A simple way the write this chunk of code is to use the list comprehension
# # Keyword method
# # new_list = [new_item for item in list]
# new_list = [n + 1 for n in numbers]

# print(new_list)

names = ['ana', 'bob', 'carl', 'dave', 'eric', 'frank']
print(names)
short_name = [name for name in names if len(name) < 4]
long_name = [name.upper() for name in names if len(name) > 3]

print(short_name[1], long_name[1])
