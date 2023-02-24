# Simple quiz game

quiz = {
    'question1': {
        'question': 'How many eyes have a human? \n A - 2 \n B - 1 \n C - 4 \n D - 0 \n',
        'answer': 'A'
    },
    'question2': {
        'question': 'Birds fly? \n A - No \n B - Maybe \n C - Yes \n D - I can fly \n',
        'answer': 'B'
    },
    'question3': {
        'question': 'Which is the capital of spain? \n A - Zaragoza \n B - Madrid \n C - Granada \n D - USA \n',
        'answer': 'B'
    },
    'question4': {
        'question': 'Is this a good game? \n A - Yes \n B - No \n C - Its the best game i have ever played \n D - Is this a game? \n',
        'answer': 'C'
    }
}

while True:
    score = 0
    max_score = 4

    print('Welcome to the quiz game!! \n')

    for key, value in quiz.items():

        print(value['question'])
        answer = input()

        if answer.lower() == value['answer'].lower():
            print('Correct!!')
            score += 1

        else:
            print('Wrong!')

    print(f'Your final score is........ \n {score} / {max_score}')
    if score == max_score:
        print('GG!!! you pass the game!')
        quit()
    else:
        restart = input('Want to try again? Y/N   ').lower()
        if restart == 'n':
            quit()
