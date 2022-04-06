# HangMan Game

import random

import hangman
import words


lives = 6


from words import word_list
chosen_word = random.choice(word_list)
# logo = hangman.stages
from hangman import logo
print(logo)

display = []
word_length = len(chosen_word)
for _ in  range(word_length):
    display += "_"
print(display)



end_of_game = False
while not end_of_game:
  guess = input("Guess the letter: ").lower()

  for position in range(word_length):
      letter = chosen_word[position]
      if letter == guess:
          display[position] = letter
     
  if guess not in chosen_word:
      lives -= 1
      from hangman import stages
      print(stages[lives])
      if lives == 0:
          print("You lost!")
          end_of_game = True    

  print(display)

  if "_" not in display:
    end_of_game = True
    print("You win!")
  # elif guess != letter:
  #   print(stages[len(missed_letters)])
  #   missed_letters += guess
  #   if len(missed_letters) == len(stages):
  #     end_of_game = True
  #     print("You lose!")
  #     print("The word was {}".format(chosen_word))
    # print(stages[len(stages) - 1])
    # print("You lose!")