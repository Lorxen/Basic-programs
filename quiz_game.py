quiz = {
    'question1': 'a',
    'question2': 'd',
    'question3': 'b',
    'question4': 'c'
}

while True:
    score = 0
    max_score = 4

    print('Welcome to the quiz game!! \n')
    answer = input('How many eyes have a human? \n A - 2 \n B - 1 \n C - 4 \n D - 0 \n').lower()
    if answer == quiz['question1']:
        score += 1
    answer = input('Birds fly? \n A - No \n B - Maybe \n C - Yes \n D - I can fly \n').lower()
    if answer == quiz['question2']:
        score += 1
    answer = input('Which is the capital of spain? \n A - Zaragoza \n B - Madrid \n C - Granada \n D - USA \n').lower()
    if answer == quiz['question3']:
        score += 1
    answer = input('Is this a good game? \n A - Yes \n B - No \n C - Its the best game i have ever played \n D - Is this a game? \n').lower()
    if answer == quiz['question4']:
        score += 1

    print(f'Your final score is........ \n {score} / {max_score}')
    if score == max_score:
        print('GG!!! you pass the game!')
        quit()
    else:
        restart = input('Want to try again? Y/N   ').lower()
        if restart == 'n':
            quit()
    


