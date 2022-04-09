from art import logo

print (logo)

def plus(n1, n2):
  return n1 + n2

def subtract (n1, n2):
  return n1 - n2

def multply (n1, n2):
  return n1 * n2

def divide (n1, n2):
  return n1 / n2

operations = {
  '+': plus,
  '-': subtract,
  '*': multply,
  '/': divide
}

numb1 = int(input('Enter first number: '))

for symbol in operations:
  print(symbol)
operation_symbol = input('Enter operation: ')
numb2 = int(input('Enter second number: '))

calc_func = operations[operation_symbol]
answer = calc_func(numb1, numb2)

print(f"{numb1} {operation_symbol} {numb2} = {answer}")