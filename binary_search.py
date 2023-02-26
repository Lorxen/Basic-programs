# Simple binary search program

# A function that takes a list and target parameters
# Multiple variables: middle, start, end, steps
# Recursion or while loop
# Increase steps each time a split is done
# Conditions to track target position

def binary_search():

    # Create a list and ask to an input
    list = []
    valors = input('Input a list of numbers separated by commas: ')
    list = valors.split(',')
    targ = input('Input a value in the list: ')

    middle = 0
    start = 0
    end = len(list)
    steps = 0

    # If target not in list we are done
    if targ not in list:
        print('Value not in list')
    else:

        # Loop while start of the list is less than the end
        while (start <= end):

            # Print the step we are and the list we are looking this moment
            print(f'Step {steps}: ', str(list[start:end+1]))
            steps = steps + 1
            middle = (start + end) // 2

            # If targ == middle we are done, else look first or second half of the list
            if targ == list[middle]:
                print(f'Found in {middle+1} position')
                start = end + 1
            elif targ < list[middle]:
                end = middle - 1
            else:
                start = middle + 1


binary_search()
