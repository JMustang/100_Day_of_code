#TODO: Create a letter using starting_letter.txt

PLACEHOLDER = '[name]'

with open('./Input/Names/invited_names.txt') as names_file:
    names = names_file.readlines()

with open('./Input/Letters/starting_letter.txt') as letter_file:
    letter = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter.replace(PLACEHOLDER, stripped_name)
        print(new_letter)

