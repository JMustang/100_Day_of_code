with open('my_file.txt') as file:
    contents = file.read()
    print(contents)


with open('my_new_file.txt', mode='w') as file:
    new_contents = file.write('Selvagem')
    print(new_contents)