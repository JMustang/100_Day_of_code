#!/bin/python


# try:
#     file = open('data.txt')
#     data_dict = {'key': 'value'}
#     print(data_dict['key'])
# except FileNotFoundError:
#     file = open('data.txt', 'w')
#     file.write('Something')
# except KeyError as error_message:
#     print(f'The key {error_message} does not exist.')
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print('File was closed')


height = float(input('Enter your height: '))
weight = int(input('Enter your weight: '))

if height > 3:
    raise ValueError('Height must be less than 3')

bmi = weight / (height ** 2)
print(f'Your BMI is {bmi}')
