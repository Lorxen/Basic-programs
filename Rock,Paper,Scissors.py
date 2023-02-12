#Rock Paper Scissors program
import random

#Function to get player and computer choice
def get_choices():
  player_choice = input('Enter a choice! Rock, Paper, Scissors: ')
  options = ['Rock', 'Paper', 'Scissors']
  computer_choice = random.choice(options)
  choices = {'player': player_choice, 'computer': computer_choice }
  
  return choices

#Function to check who wins the match
def check_win(player, computer):
  print (f'You chose: {player}, computer chose: {computer}')
  if player == computer:
    return "It's a tie!"
  elif player == 'Rock':
    if computer == 'Scissors':
      return 'Rock smashes scissors! You win!'
    else: 
      return 'Paper covers rock! You lose!'
  elif player == 'Paper':
    if computer == 'Scissors':
      return 'Paper gets cut by scissors! You lose!'
    else: 
      return 'Paper covers rock! You win!'
  elif player == 'Scissors':
    if computer == 'Rock':
      return 'Rock smashes scissors! You lose!'
    else: 
      return 'Paper gets cut by scissors! You win!'
  else:
    return 'Not valid imput'

#Beginning of the program
choices = get_choices()
result = check_win(choices['player'], choices['computer'])

#Loop until player wants to quit
while True: 
  if result == 'Not valid imput':
    print ('ERROR: Not valid input')
    choices = get_choices()
    result = check_win(choices['player'], choices['computer'])
    continue
  else:
    print (result)
    print ('Do you want to play again? YES/NO')
    answer = input()
    if answer != 'YES':
      break
    else:
      choices = get_choices()
      result = check_win(choices['player'], choices['computer'])
    
