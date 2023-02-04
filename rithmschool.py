# Create a deck of cards class. Internally, the deck of cards should use another class, a card class.
# Deck class should have a deal method to deal a single card from the deck
# After a single card is dealt, remove it from the deck
# Create a shuffle method which makes sure the deck of cards has all 52 cards, and then rearranges them randomly
# The Card class should have a suit and a value
import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

class Deck:
    def __init__(self):
        suits = ['Hearts','Diamonds','Spades','Clubs']
        values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        self.cards = [Card(suit, value) for suit in suits for value in values] # for every suit in suits, go through every value in values & apply them to the suits
    
    def deal(self):
        if len(self.cards) == 0:
            return "All cards have been dealt"
        return self.cards.pop()

    def shuffle(self):
        if len(self.cards) < 52:
            return "This deck is not full"
        random.shuffle(self.cards) # imported shuffle built-in method from random
        return self