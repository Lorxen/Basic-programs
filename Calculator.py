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


operation = []
result = 0
exit = False
next = ''

while exit == False:

    n = input('Please enter an operation with +, -, * or / separate with spaces: ')

    operation = n.split()
    operate = True

    while operate == True:

        if operation[1] == '+':
            result = int(operation[0]) + int(operation[2])

        elif operation[1] == '-':
            result = int(operation[0]) - int(operation[2])

        elif operation[1] == '*':
            result = int(operation[0]) * int(operation[2])

        else: result = int(operation[0]) / int(operation[2])

        print(result)
        next = input('(+  -  *  /)  CLEAR  EXIT : ').lower()

        if next == 'exit':
            exit = True
            operate = False
        
        elif next == 'clear':
            operate = False

        else:
            operation = next.split()
            operation.insert(0,result)