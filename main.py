from password_art import art
import random

print(art)

letters = [
  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
  'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
  'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
  'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
letters_number = int(input("How many letters would you like in your password?\n"))
symbols_number = int(input("How many symbols would you like?\n"))
numbers_number = int(input("How many numbers would you like?\n"))
password1 = []
for char in range(1, letters_number + 1):
  random_char = random.choice(letters)
  password1 += random_char
for number in range(1, numbers_number + 1):
  random_number = random.choice(numbers)
  password1 += random_number
for symbol in range(1, symbols_number + 1):
  random_symbol = random.choice(symbols)
  password1 += random_symbol
random.shuffle(password1)
password = ""
for last in password1:
  password += last
print("Your password:", password)