# Super simple black jack app
# Phase 1 - one round of cards, hit or stand. Dealer hits on soft 17. Single deck
# Help for creating deck: https://medium.com/@anthonytapias/build-a-deck-of-cards-with-oo-python-c41913a744d3 

import random
card_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
card_number = random.choice(card_list)
print (str(card_number))

class Card(object):
    def __init__(self, suit, cardValue):
        self.suit = suit
        self.CardValue = cardValue


class Deck(object):
    def __init__(self, numberOfCards):
        self.numberOfCards = 0

class PlayerCards(object):
    def __init__(self, playerFirstCard, playerSecondCard):
        self.playerFirstCard = 0
        self.playerSecondCard = 0

class DealerCards(object):
    def __init__(self, dealerUpCard, dealerDownCard):
        self.dealerUpCard = card_number
        self.dealerDownCard = card_number


PlayerHand = PlayerCards(card_number, card_number, card_number, card_number)
print(PlayerHand.PlayerFirstCard, PlayerHand.PlayerSecondCard, PlayerHand.DealerUpCard, PlayerHand.DealerDownCard)

#random change 2