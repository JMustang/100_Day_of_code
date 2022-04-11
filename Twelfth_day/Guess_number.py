from art import logo
print(logo)

import random

name = input("What is your name? ")
print(f"Hello {name}, i`m thinking of a number between 1 and 100, you have 10 tries to guess it.")

guessing = 10
random_number = random.randint(1, 100)

while guessing > 0:
  guess = int(input(f"Ok {name}, guess a number: "))
  if guess == random_number:
      print("You guessed it!")
      break
  elif guess > random_number:
      print("Too high!")
  elif guess < random_number:
      print("Too low!")
  guessing -= 1
  if guessing == 0:
      print("You lost!")
      print(f"The number was {random_number}")
      break
  print(guessing)
