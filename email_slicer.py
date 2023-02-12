#collect email from user
#split the email using the @, the first part as the user name the second part is gonna be saced as domain
#spit domain using ., 

def main():

    print('Welcome to the email slicer! \n')
    lop = True

    while lop == True:

        valid = True
        while valid == True:

            email_input = input('Please input your email: ')
            print()
            user_name = email_input.split('@')

            if len(user_name) == 2:
                domain = user_name[1].split('.')
                if len(domain) == 2:
                    valid = False
                else:
                    print('NOT VALID INPUT\n')
            else:
                print('\nNOT VALID INPUT\n')

        print('Username: ', user_name[0])
        print('Domain: ', domain[0])
        print('Extension: ', domain[1])
        print()
        end = False
        while end == False:
            cont = input('Continue? Y/N: ').lower()
            print()
            if cont == 'y':
                end = True
            elif cont == 'n':
                end = True
                lop = False
            else:
                print('NOT VALID INPUT\n')


main()