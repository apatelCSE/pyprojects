from enum import Enum
from enum import IntEnum
from random import *

entire_deck = []
partial_deck = []
player1_cards = []
player2_cards = []

#This class defines the card enum for playing cards
class Card(IntEnum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14

#This class defines the suit enum for playing cards
class Suit(Enum):
    SPADES = 'spades'
    CLUBS = 'clubs'
    HEARTS = 'hearts'
    DIAMONDS = 'diamonds'

#This class holds information about the playing cards.
class PlayingCards:
    def __init__(self, card_value, card_suit):
        self.card = card_value
        self.suit = card_suit

#This function deals the entire deck of cards.
def create_deck():
    for suit in Suit :
        for card in Card:
            entire_deck.append(PlayingCards(Card(card), Suit(suit)))
    return entire_deck

#Draws a single card from the deck.
def draw_card(deck):
    random_card = randint(0, len(deck) -1)
    return deck.pop(random_card)

#Deals players for a game of war.
def deal_war():
    while(len(partial_deck) > 0):
        player1_cards.append(draw_card(partial_deck))
        player2_cards.append(draw_card(partial_deck))

create_deck()
partial_deck = list(entire_deck)
deal_war()

p1counter = 0
p2counter = 0

for i in range(0, len(player1_cards)):
    if (player1_cards[i].card > player2_cards[i].card):
        print("Player 1 wins with a ", player1_cards[i].card)
        print("Player 2 loses with a ", player2_cards[i].card)
        p1counter += 1
    if (player1_cards[i].card < player2_cards[i].card):
        print("Player 1 loses with a ", player1_cards[i].card)
        print("Player 2 wins with a ", player2_cards[i].card)
        p2counter+= 1
    else:
        print("WAR.")

print("Player 1 Final Score: ", p1counter)
print("Player 2 Final Score: ", p2counter)

if p1counter < p2counter:
    print("Player 2 wins!")
if p1counter > p2counter:
    print("Player 1 wins!")
