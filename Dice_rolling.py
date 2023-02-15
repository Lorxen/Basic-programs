# Import random
# Define a funtion to roll the dice
# Create a dictionary that will have the drawins of the dice
# Loop asking if want to roll the dice

import random

def roll():

    drawins = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    )
}

    print('\n \tWelcome to roll the dice program!\n')

    while True:

        while True:
            ask = input('\nDo you want to roll the dice?  Y/N  ').lower()
            if ask == 'n':
                quit()
            elif ask == 'y':
                break
            else:
                print('\nNOT VALID INPUT')

        result1 = random.randint(1,6)
        result2 = random.randint(1,6)

        print(f'\nDice rolled: {result1} and {result2}\n')
        print('\n'.join(drawins[result1]))
        print()
        print('\n'.join(drawins[result2]))

roll()
    








