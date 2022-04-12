from tokenize import Name


def greet():
  print("Hello")
  print("How are you?")
  print("Isn`t the weather nice today?")
greet()


# def tell_me_your_name(name):
#   print("Hello " + name)
# tell_me_your_name("Junior")

def greet_with(name, location):
  print(f"Hello {name} from {location}")
greet_with(location="Satuba", name="junior")


def greet(name):
  Name = input("What is your name?\n")
  print(f"Hello {Name}")
greet(name=Name)