import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
Rock
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
Paper
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
Scissors
'''

game_images = [rock, paper, scissors]
#Write your code below this line 👇

me_choice = int(input("Type 0 for rock, 1 for paper, 2 for scissors: "))

if me_choice >= 3 or me_choice < 0:
    print("Invalid choice, you lose!")
else:
  print(game_images[me_choice])

  oponente = int(random.randint(0,2))
  print(game_images[oponente])

  print(me_choice)
  print(oponente)

  if me_choice == oponente:
      print("It's a tie!")
  elif me_choice == 0 and oponente == 1:
      print("Paper covers rock. You lose!")
  elif me_choice == 0 and oponente == 2:
      print("Rock breaks scissors. You win!")
  elif me_choice == 1 and oponente == 0:
      print("Paper covers rock. You win!")
  elif me_choice == 1 and oponente == 2:
      print("Scissors cuts paper. You lose!")
  elif me_choice == 2 and oponente == 0:
      print("Rock breaks scissors. You lose!")
  elif me_choice == 2 and oponente == 1:
      print("Scissors cuts paper. You win!")
  else:
      print("Something went wrong")
