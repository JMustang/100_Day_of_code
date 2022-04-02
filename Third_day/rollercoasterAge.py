print('Welcome to the rollercoaster!')
height = int(input('How tall are you in cm? '))
bill = 0

if height > 120:
    print('You can ride the rollercoaster!')
    age = int(input('What is your age? '))
    if age < 12:
        bill = 5
        print('Child tickets are $5.')
    elif age <= 18:
        bill = 7
        print('Youth tickets are $7.')
    else:
      bill = 12
      print('Adolt tickets are $12.')

    wants_ticket = input('Do you want a photo taken? Y or N. ')
    if wants_ticket == 'y':
      bill += 3

    print(f'Your final bill is ${bill}.')
      
else:
  print('Sorry, you have to grow taller before you can ride.')