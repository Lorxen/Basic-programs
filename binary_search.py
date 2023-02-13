# A function that takes a list and target parameters
# Multiple variables: middle, start, end, steps
# Recursion or while loop
# Increase steps each time a split is done
# Conditions to track target position

def binary_search(list, targ):

    middle = 0
    start = 0
    end = len(list)
    steps = 0

    if list == []:
        print('Enter a valid list')
    elif targ not in list:
        print('Value not in list')
    else:
        while (start <= end):
            
            print(f'Step {steps}: ', str(list[start:end+1]))
            steps = steps + 1
            middle = (start + end) // 2

            if targ == list[middle]:
                return middle
            elif targ < list[middle]:
                end = middle - 1
            else:
                start = middle + 1

list = []
inp = input('Input a list of numbers: ')
list = inp.split()
num = input('Input a number in the list: ')
binary_search(list,num)

