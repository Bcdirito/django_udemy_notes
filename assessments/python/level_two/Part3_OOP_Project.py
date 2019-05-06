#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

def full_deck():
    full = []

    for s in SUITE:
        for r in RANKS:
            full.append(r + s)
    
    return full

class Deck():
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """
    original_deck = full_deck()

    def split_deck(self):
        shuffle(self.original_deck)
        if len(self.original_deck) == 52:
            first_half = self.original_deck[0:26]
            self.original_deck = self.original_deck[26:]
            return first_half
        else:
            second_half = self.original_deck[0:]
            self.original_deck = []
            return second_half

class Hand(Deck):
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    pass

    def __init__(self, Deck):
        self.hand = self.split_deck()

    def add_cards(self, new_cards, personal_cards):
        all_cards = new_cards + personal_cards
        self.remove_cards(personal_cards)
        for c in all_cards:
            self.hand.append(c)

    def remove_cards(self, cards):
        if (len(cards) > 1):
            new_origin = self.hand.index(cards[-1]) + 1
            self.hand = self.hand[new_origin:]
        else:
            self.hand.pop(0)

        

class Player(Hand):
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """
    pass

    def __init__(self, name, Hand):
        self.name = name
        self.hand = Hand.hand


def play_game(computer, human):
    computer_card = get_value(computer.hand[0])
    human_card = get_value(human.hand[0])

    if computer_card > human_card:
        human.remove_cards([human.hand[0]])
        computer.add_cards([human.hand[0]], [computer.hand[0]])
    elif human_card > computer_card:
        computer.remove_cards([computer.hand[0]])
        human.add_cards([computer.hand[0]], [human.hand[0]])
    else:
        tie_breaker(computer, human)

def get_value(card):
    face_cards = {
        "J": 10,
        "Q": 11,
        "K": 12,
        "A": 13
    }

    face_list = ["J", "Q", "K", "A"]

    if card[0] not in face_list:
        return int(card[0])
    else:
        return face_cards[card[0]]

def tie_breaker(computer, human):
    computer_pile = computer.hand[0:4]
    human_pile = human.hand[0:4]

    computer_card = get_value(computer_pile[-1])
    human_card = get_value(human_pile[-1])

    if computer_card > human_card:
        human.remove_cards(human_pile)
        computer.add_cards(human_pile, computer_pile)
    elif human_card > computer_card:
        computer.remove_cards(computer_pile)
        human.add_cards(computer_pile, human_pile)
    else:
        double_tie_breaker(computer, human, (len(human_pile) + 2))

def double_tie_breaker(computer, human, total):
    computer_pile = computer.hand[0:total]
    human_pile = human.hand[0:total]

    computer_card = get_value(computer_pile[-1])
    human_card = get_value(human_pile[-1])

    if computer_card > human_card:
        human.remove_cards(human_pile)
        computer.add_cards(human_pile, computer_pile)
    elif human_card > computer_card:
        computer.remove_cards(computer_pile)
        human.add_cards(computer_pile, human_pile)
    else:
        total += 2
        double_tie_breaker(computer, human, total)


    


######################
#### GAME PLAY #######
######################

d = Deck()
print("Welcome to War, let's begin...")

# Use the 3 classes along with some logic to play a game of war!
user_name = input("What is your name? ")
user_hand = Hand(d)
computer_hand = Hand(d)
computer = Player("Computer", computer_hand)
user = Player(user_name, user_hand)

print("Welcome {name}".format(name = user.name))
print("Let's play a game of war!")

while (len(user.hand) < 52 and len(computer.hand) < 52):
    play_game(computer, user)
else:
    if len(user.hand) == 52:
        print("Congrats {name}".format(name = user.name))
    else:
        print("Uh Oh! The Computer Won!")
