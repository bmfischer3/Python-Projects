
# Practice found here: http://introtopython.org/classes.html
# Exercise found here: https://www.rithmschool.com/courses/python-fundamentals-part-2/python-object-oriented-programming-exercises



class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def show(self):
        print ("{} of {}".format(self.value, self.suit))

# After having created the Card class, I have created objects to hold the card values
# The show(self) method allows me to print the value of the card. 

card = Card("Card,", 6)
card.show()

# The above creates the card variable that references the show method. 
# The show() is an empty object, so it references what is in the card("Card,", 6)

class Shoe:
    def __init__(self):
        self.cards = []
        self.build()

# Have initiatilized the Deck class to contain a list, self.cards = []
# Have initialized the self.build() object, althoguh it does not yet know what to do
    
    def build(self):
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for v in range (1,14):
                self.cards.append(Card(s, v))

# Here the build(self) object is given instruction on what to do. 
    def show(self):
        for c in self.cards:
            c.show()


# 

# deck = Deck()
# deck.show()

class Player:
    def __init__(self):
        pass

class Dealer:
    def __init__(self):
        pass


