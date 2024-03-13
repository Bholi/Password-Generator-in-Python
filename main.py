import random

print('Welcome to Password Generator Program !')

alpha_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '[', ']']

alpha_input = int(input('How many alphabet you want ? : '))
number_input = int(input('How many number you want ? : '))
symbol_input = int(input('How many symbols you want ? : '))

password_list = []
for i in range(0, alpha_input):
    password_list += random.choice(alpha_letters)
for j in range(0, number_input):
    password_list += random.choice(number)
for k in range(0, symbol_input):
    password_list += random.choice(symbols)
password = ''
random.shuffle(password_list)
for m in password_list:
    password += m
print(f'Your password is : {password}')
