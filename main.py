import random
import string


print("Welcome to the PyPassword Generator")
letter_count = int(input("How many letters would you like in your password?\n"))
symbol_count = int(input("How many symbol would you like in your password?\n"))
number_count = int(input("How many numbers would you like in your password?\n"))

numbers_list = [1,2,3,4,5,6,7,8,9,0]
letters_list = list(string.ascii_letters)
symbols_list = ["!","@","#","$","%","^","&","*","(",")","_","+"]

password = ""
password_list = []


for char in range(1, letter_count + 1):
    password_list.append(random.choice(letters_list))

for num in range(1, number_count + 1):
    password_list.append(random.choice(numbers_list))

for sym in range(1, symbol_count + 1):
    password_list.append(random.choice(symbols_list))


random.shuffle(password_list)
for char in password_list:
    password += str(char)

print(password)