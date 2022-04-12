# !/usr/bin/env python3

# Describe a problem:

# def my_func():
#   for i in range(1, 20):
# # the 'if' is never True
#     if i == 20 - 1:
#       print('You got it')
# my_func()

# from random import randint
# dice_imgs = ["1", "2", "3", "4", "5", "6"]
# # dice_num = randint(0, 5)
# # this line is wrong
# # the correct range is 0 to 5
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])

# year = int(input('What your year of birth? '))
# if year >= 1980 and year <= 1994:
#   print('You are a millenial')
# elif year >= 1994:
#   print('You are a Gen Z')

# age = int(input('How old are you? '))
# if age >= 18:
#   print(f'You can drive at age of {age}')


# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(f"Total words: {total_words}")


number = int(input("Enter a number: "))

if number % 2 == 0:
  print("this is a even Number ")
else:
  print("this is a odd Number ")