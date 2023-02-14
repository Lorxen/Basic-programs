# Ask user if they want to generate a passowrd or not
# If yes, ask for password lenght
# Generate password
# Print password
# If initial response is no, exit program

import string
import random

characters = list(string.ascii_letters + string.digits + '!@#$%^&*()')

def generate_password():

    while True:
        try:
            pas_len = int(input('\nHow long would you like your password to be? '))
            break
        except:
            print('\nNOT VALID INPUT')
    
    pas = []
    random.shuffle(characters)

    for i in range(pas_len):
        pas.append(random.choice(characters))

    random.shuffle(pas)
    pasw = ''.join(pas)
    print('\n' + pasw + '\n')

while True:

    option = input('Do you want to generate a password?  Y/N  ').lower()
    if option == 'y':
        generate_password()
    elif option == 'n':
        quit()
    else:
        print('\nNOT VALID INPUT\n')

kl