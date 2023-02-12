# Define the functions needed: add, sub, mul, div
# Print options to the user
# Ask for values
# Call the functions
# While loop to continue the program until the user wants to exit

def add(num1,num2):
    return num1 + num2

def sub(num1,num2):
    return num1 - num2

def mult(num1,num2):
    return num1 * num2

def div(num1,num2):
    return num1 / num2

def is_number(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

#Set parameters to start program
operation = []
result = 0
exit = False
next = ''
inp = True

#While not exit keep running
while exit == False:

    n = input('Please enter an operation with +, -, * or / separate with spaces: ')

#Split imput in number function number, then check if input is correct

    operation = n.split() 

    if operation != [] and is_number(operation[0]) and is_number(operation[2]) and (operation[1] == '+' or operation[1] == '-' or operation[1] == '*' or operation[1] == '/'):
        operate = True

    else: 
        operate = False
        print('NOT VALID INPUT')

#While input is correct, apply the calculation

    while operate == True:

        if operation[1] == '+':
            result = float(operation[0]) + float(operation[2])

        elif operation[1] == '-':
            result = float(operation[0]) - float(operation[2])

        elif operation[1] == '*':
            result = float(operation[0]) * float(operation[2])

        else: result = float(operation[0]) / float(operation[2])

        print(result)
        contin = True

#Ask for continue, clear or exit

        while contin == True:

            next = input('(+  -  *  /)  CLEAR  EXIT : ').lower()

            if next == 'exit':
                exit = True
                operate = False
                contin = False
            
            elif next == 'clear':
                operate = False
                contin = False

#If not exit or clear, check if new operation input is valid

            else:
                operation = next.split()
                if operation != [] and (operation[0] == '+' or operation[0] == '-' or operation[0] == '*' or operation[0] == '/') and is_number(operation[1]):
                    contin = False
                    operation.insert(0,result)

                else: 
                    print('NOT VALID INPUT')
                    