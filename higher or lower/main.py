from unicodedata import decimal
import random

NCARDS = 8
INIT_SCORE = 50
SUIT_TUPLE = ("Clubs", "Diamonds", "Hearts", "Spades")
RANK_TUPLE = ("Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King")
card1 = {"rank" : "Jack", "suit" : "Spades", "value" : 11}
card2 = {"rank" : "5", "suit" : "Clubs", "value" : 5}
cardList = [card1, card2]

def createDeck():
    deck = []
    # for i in range(len(SUIT_TUPLE)):
    #     for j in range(len(RANK_TUPLE)):
    #         card = {"suit" : SUIT_TUPLE[i], "rank" : RANK_TUPLE[j], "value" : j+1}
    #         deck.append(card)
    for suit in SUIT_TUPLE:
        for value, rank in enumerate(RANK_TUPLE):
            card = {"suit" : suit, "rank" : rank, "value" : value+1}
            deck.append(card)
    return deck

deckList = createDeck()

def shuffleCards(deck):
    random.shuffle(deck)
    return deck

deckList = shuffleCards(deckList)

def getCard(deck):
    card = deck.pop()
    return card

card = getCard(deckList)
print(card)

