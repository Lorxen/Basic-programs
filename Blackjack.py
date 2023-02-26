# Blackjack game with use of lists
import random


# CARD CLASS CONFIGURATION
class Card:

    # Initialize the card with a suit and rank values
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    # Configuration of the class call
    def __str__(self):
        return f'{self.rank["rank"]} of {self.suit}'


# DECK CLASS WITH SHUFFLE AND DEAL FUNCTIONS
class Deck:

    # Default deck configuration when created
    def __init__(self):
        self.cards = []
        suits = ['spades', 'clubs', 'hearts', 'diamonds']
        ranks = [
            {'rank': 'A', 'value': 11},
            {'rank': '2', 'value': 2},
            {'rank': '3', 'value': 3},
            {'rank': '4', 'value': 4},
            {'rank': '5', 'value': 5},
            {'rank': '6', 'value': 6},
            {'rank': '7', 'value': 7},
            {'rank': '8', 'value': 8},
            {'rank': '9', 'value': 9},
            {'rank': '10', 'value': 10},
            {'rank': 'J', 'value': 10},
            {'rank': 'Q', 'value': 10},
            {'rank': 'K', 'value': 10},
        ]

        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    # Shuffle function for deck
    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    # Deal function for deck
    def deal(self, number):
        cards_dealt = []
        for x in range(number):
            if len(self.cards) > 0:
                card = self.cards.pop()
                cards_dealt.append(card)
        return cards_dealt


# HAND CLASS
class Hand:

    # Hand default configuration
    def __init__(self, dealer=False):
        self.cards = []
        self.value = 0
        self.dealer = dealer

    # Add card to hand function
    def add_card(self, card_list):
        self.cards.extend(card_list)

    # Calculate value of the hand
    def calculate_value(self):
        self.value = 0
        has_ace = False

        for card in self.cards:
            card_value = int(card.rank['value'])
            self.value += card_value
            if card.rank['rank'] == 'A':
                has_ace = True
        if has_ace and self.value > 21:
            self.value -= 10

    # Get value of the hand
    def get_value(self):
        self.calculate_value()
        return self.value

    # Look if is blackjack
    def is_blackjack(self):
        return self.get_value() == 21

    # Display the hand
    def display(self, show_all_dealer_cards=False):
        print(f'''{"Dealer's" if self.dealer else "Your"} hand: ''')
        for index, card in enumerate(self.cards):
            if index == 0 and self.dealer and not show_all_dealer_cards and not self.is_blackjack():
                print('Hidden')
            else:
                print(card)

        if not self.dealer:
            print('Value', self.get_value())
            print()


# CLASS GAME
class Game:

    def play(self):
        game_number = 0
        games_to_play = 0
        while games_to_play <= 0:
            try:
                games_to_play = int(
                    input('How many games do you want to play? '))
            except:
                print('You must enter a number!')
        while game_number < games_to_play:
            game_number += 1
            deck = Deck()
            deck.shuffle()
            self.player_hand = Hand()
            self.dealer_hand = Hand(dealer=True)

            for i in range(2):
                self.player_hand.add_card(deck.deal(1))
                self.dealer_hand.add_card(deck.deal(1))

            print()
            print('*' * 30)
            print(f'Game {game_number} of {games_to_play}')
            print('*' * 30)
            self.player_hand.display()
            self.dealer_hand.display()

            if self.check_winner(self.player_hand, self.dealer_hand):
                continue

            choice = ''
            while self.player_hand.get_value() < 21 and choice not in ['s', 'stand']:
                choice = input('Please choose Hit or Stand').lower()
                print()
                while choice not in ['s', 'h', 'hit', 'stand']:
                    choice = input(
                        'Please choose Hit or Stand or (H/S)').lower()
                    print()
                if choice in ['h', 'hit']:
                    self.player_hand.add_card(deck.deal(1))
                    self.player_hand.display()

            if self.check_winner(self.player_hand, self.dealer_hand):
                continue

            player_hand_value = self.player_hand.get_value()
            dealer_hand_value = self.dealer_hand.get_value()

            while dealer_hand_value < 17:
                self.dealer_hand.add_card(deck.deal(1))
                dealer_hand_value = self.dealer_hand.get_value()

            self.dealer_hand.display(show_all_dealer_cards=True)

            if self.check_winner(self.player_hand, self.dealer_hand):
                continue

            print('Final results: ')
            print('Your hand:', player_hand_value)
            print('Dealer hand:', dealer_hand_value)

            self.check_winner(player_hand_value, dealer_hand_value, True)

        print('\n Thanks for playing!!')

    # Check winner function inside game class
    def check_winner(self, player_hand, dealer_hand, game_over=False):
        if not game_over:
            if self.player_hand.get_value() > 21:
                print('You busted! Dealer wins!')
                return True
            elif self.dealer_hand.get_value() > 21:
                print('Dealer busted! You win!!')
                return True
            elif self.dealer_hand.is_blackjack() and self.player_hand.is_blackjack():
                print('Both players have blackjack! Its a tie!')
                return True
            elif self.dealer_hand.is_blackjack():
                print('Dealer has blackjack! He wins!!')
                return True
            elif self.player_hand.is_blackjack():
                print('You have blackjack! You win!!')
                return True
        else:
            if self.player_hand.get_value() > self.dealer_hand.get_value():
                print('You win!!!')
            elif self.player_hand.get_value() == self.dealer_hand.get_value():
                print('Its a tie!')
            else:
                print('Dealer wins!!')
            return True
        return False


# CODE BEGINS
g = Game()
g.play()
