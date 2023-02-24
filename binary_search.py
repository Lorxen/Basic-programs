# Simple binary search program

# A function that takes a list and target parameters
# Multiple variables: middle, start, end, steps
# Recursion or while loop
# Increase steps each time a split is done
# Conditions to track target position

def binary_search():

    list = []
    valors = input('Input a list of words or numbers separated by commas: ')
    list = valors.split(',')
    targ = input('Input a value in the list: ')

    middle = 0
    start = 0
    end = len(list)
    steps = 0

    if targ not in list:
        print('Value not in list')
    else:

        while (start <= end):

            print(f'Step {steps}: ', str(list[start:end+1]))
            steps = steps + 1
            middle = (start + end) // 2

            if targ == list[middle]:
                print(f'Step {steps}: ', str(list[middle]))
                print(f'Found in {middle+1} position')
                start = end + 1
            elif targ < list[middle]:
                end = middle - 1
            else:
                start = middle + 1


binary_search()
