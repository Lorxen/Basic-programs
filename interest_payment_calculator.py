# Collect the necessary inputs: principal, apr, years
# Calculate the monthly payment
# Show to the user

def main():

    while True:
        try:
            principal = float(input('Input the lian amount: '))
            apr = float(input('Input the annual interest rate: '))
            years = int(input('Input amount of yars: '))
            break
        except:
            print('\nNOT VALID INPUT\n')

    monthly_interest_rate = apr / 1200
    amount_of_months = years * 12
    monthly_payment = principal * monthly_interest_rate / \
        (1 - (1 + monthly_interest_rate) ** (-amount_of_months))

    print('\nThe monthly payment for this loan is: %.2f' %
          monthly_payment + ' $')
    print()


print('\tThis is a monthly payment loan calculator \n')
while True:
    main()
    correct = True
    while correct == True:
        inp = input('Restart or Exit?  R/E  ').lower()
        print('')
        if inp == 'e':
            quit()
        elif inp == 'r':
            correct = False
        else:
            print('\n NOT VALID INPUT')
