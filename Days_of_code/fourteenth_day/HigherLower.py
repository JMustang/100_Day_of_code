from art import logo, vs
from game_data import data as dt
import random


def format_data(account):

  """Format the account data into printable format"""
  account_name = account['name']
  account_descr = account['description']
  account_country = account['country']
  return f'{account_name}, a {account_descr}, from {account_country}'


# Use if Statement to check if the guess is correct
def  check_answer(guess, a_followers, b_followers):
  """Take the user guess and follower counts and returns if got """
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"


# Print the logo
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(dt)

while game_should_continue:
  # Generate a random account from the game data



  # Generate a random account from the game data
  account_a = account_b
  account_b = random.choice(dt)
  
  while account_a == account_b:
      account_b = random.choice(dt)

  print(f'Account A: {format_data(account_a)}')
  print(vs)
  print(f'Account B: {format_data(account_b)}')


  # Ask user for a guess
  guess = input('Who has more followers? Type A or B: ').lower()

  # Check if user is correct
  # Get the follower count of each account
  a_follower_count = account_a['follower_count']
  b_follower_count = account_b['follower_count']


  is_correct = check_answer(guess, a_follower_count, b_follower_count)

  # Give user feedback on their guess
  if is_correct:
    score += 1
    print(f'You are correct! Current score: {score}')
  else:
    game_should_continue = False
    print(f'Sorry, that is not correct. Final score: {score}')

  # Ask user if they want to continue