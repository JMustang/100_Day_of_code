# import random

# n = random.randint(1, 100)
 
# while (guess != n):
#   guess = int(input("Guess a number between 1 and 100: "))
#   if n > guess:
#       print("Too low - try again")
#   elif n < guess:
#       print("Too high - try again")
#   else:
#       print("You got it!")

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# name = fruits[-5]
# print(name)
# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# fruits[-1] = "Melons"
# fruits.append("Lemons")
# print(fruits)
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]
 
print(dirty_dozen[1][1])