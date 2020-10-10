#########################################
#  Blackjack Python   |                 #
#########################################

import random
import sys


# Game Class
class Game:
    def __init__(self):
        self.budget = 500
        self.currentBet = 0
        self.player_mode = 'stay'
        self.dealer_mode = 'stay'
        self.player = []
        self.dealer = []
        self.player_score = 0
        self.dealer_score = 0
        self.cards = []

    def pass_cards(self, to=None, times=1):
        # pass cards to player and user
        for i in range(times):
            index = random.randint(0, len(self.cards) - 1)

            if to == 'dealer':
                self.dealer.append(self.cards[index])

            else:
                self.player.append(self.cards[index])

            self.dealer_score = sum(list(map(lambda x: x.value, self.dealer)))
            self.player_score = sum(list(map(lambda x: x.value, self.player)))

            self.cards.pop(index)

        cards = list(map(lambda x: x.name, self.dealer if to == 'dealer' else self.player))

        if to == 'dealer' and times == 2:
            print(f"dealer got {' and '.join([cards[0], '?'])}\n")
        elif to == 'dealer' and times == 1:
            print(f"dealer got {' and '.join(cards)}\ndealer score is {self.dealer_score}")
        else:
            print(f'you got {" and ".join(cards)}\nyour score is {self.player_score}')

    def create_cards(self):
        deck = Deck()
        self.cards = deck.create_deck()
        random.shuffle(self.cards)
        self.player_mode = 'stay'
        self.dealer_mode = 'stay'
        self.player = []
        self.dealer = []
        self.player_score = 0
        self.dealer_score = 0

    def hit_or_stay(self):
        while True:
            if self.player_score > 21:
                print('\n\nYou bust.....You lost the bet\n\n')
                return 'lose'

            choice = input('\n\nWould u like to hit or stay??\nto hit press \'h\'\nto stay press anything except h')

            if choice == 'h':
                print('\nYou chose to hit....\n')
                self.player_mode = 'hit'
                self.pass_cards(times=1)
                continue

            else:
                print('\nYou chose to stay....\n')
                break

        while True:
            if self.dealer_score > 21:
                print('\n\ndealer bust.....You won the bet\n\n')
                return 'won'

            self.dealer_mode = ['hit', 'stay', 'hit', 'stay', 'hit'][random.randint(0, 4)]
            print(f'\ndealer chose to {self.dealer_mode}....\ndealer score is {self.dealer_score}\n')

            if self.dealer_mode == 'hit':
                self.pass_cards('dealer', 1)
                continue
            else:
                break

        if self.player_score > self.dealer_score:
            print(f'\n\nyour score is {self.player_score}\nU won the bet\n\n')
            return 'won'
        elif self.player_score < self.dealer_score:
            print(f'\n\nyour score is {self.player_score}\nYou Lost the bet\n\n')
            return 'lose'
        else:
            print('\n\ntie\n\n')
            return 'tie'

    # start the game
    def start(self):
        if self.budget <= 0:
            print('\n\nYou lost all your money!!!!\n\nThanks for playing')
            sys.exit()
        while True:
            try:
                print(f"current budget = {self.budget}")
                self.currentBet = int(input("How much u would like to bet???\n"))
                if self.budget >= self.currentBet:
                    self.budget -= self.currentBet
                    break
                else:
                    raise ValueError('A very specific bad thing happened')

            except Exception:
                print("invalid value.....")

        self.create_cards()

        self.pass_cards(times=2)
        self.pass_cards('dealer', 2)

        result = self.hit_or_stay()

        if result == 'won':
            self.budget += (self.currentBet * 2)
        elif result == 'tie':
            self.budget += self.currentBet
        else:
            self.budget = self.budget


class Deck:
    def __init__(self):
        self.cards = []

    def create_deck(self):
        suits = ['diamonds', 'clubs', 'spades', 'hearts']
        for i in range(2, 11):
            for x in range(4):
                card = Card(i, f'{i} of {suits[x]}')
                self.cards.append(card)
        for i in range(4):
            card = Card(10, f'king of {suits[i]}')
            self.cards.append(card)
            card = Card(10, f'Queen of {suits[i]}')
            self.cards.append(card)
            card = Card(10, f'Jack of {suits[i]}')
            self.cards.append(card)
            card = Card(11, f'Ace of {suits[i]}')
            self.cards.append(card)

        return self.cards


class Card:
    def __init__(self, value, name):
        self.value = value
        self.name = name


game = Game()


while True:
    game.start()
