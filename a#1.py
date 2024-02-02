import random

#Class Card
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return f"{self.rank} of {self.suit}"
 
#class deck
class Deck:
    #using python list
    #defining suits and cards ranks or names
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
   
    def __init__(self):
        #creating instance of Card class and passing suits ranks as arguments
        self.cards = [Card(suit, rank) for suit in self.suits for rank in self.ranks]
   
    def shuffleDeck(self):
        #shuffling deck
        random.shuffle(self.cards)
   
    def deal(self):
        return self.cards.pop()    


#class dealer
class Dealer:  
    def __init__(self):
        self.hand = []
        self.total = 0
        
    def showHoleCard(self):
        print("Dealer's hole card:", self.hand[1])

    def hitUntil17(self):
        if(self.total<17): return True ; return False
        
       #class player 
class Player:
    def __init__(self):
        self.hand = []
        self.total = 0

    def hitOrStand(self):
        return input("Do you want to HIT(PRESS \"H\") or STAND (PRESS \"S\") ? ").lower().startswith('h')
    
#class game(or table or world)
class Game:
    def decideWinner(playerTotal, dealerTotal):
        print(f"Player's Total: {playerTotal}")
        print(f"Dealer's Total: {dealerTotal}")
        if playerTotal > 21 or (dealerTotal <= 21 and dealerTotal > playerTotal):
            return "!!!DEALER WINS!!!"
        elif dealerTotal > 21 or (playerTotal > dealerTotal and playerTotal <= 21):
            return "!!!PLAYER WINS!!!"
        elif playerTotal == 21 or dealerTotal == 21:
            return "!!!BLACKJACK!!!"
        else:
            return "!!!DRAW!!!"    


#function to return card values according to the names or ranks
def card_value(rank):
        if rank in ['Jack', 'Queen', 'King']:
            return 10
        elif rank == 'Ace':
            return 11
        else:
            return int(rank)
        
#main module
def main():
    printBars()
    print("\t \t WELCOME TO BLACKJACK")
    printBars()
    deck = Deck()
    deck.shuffleDeck()

    player = Player()
    dealer = Dealer()

    # Initial deal
    for i in range(2):
        player.hand.append(deck.deal())
        dealer.hand.append(deck.deal())

    player.total = sum(card_value(card.rank) for card in player.hand)
    dealer.total = sum(card_value(card.rank) for card in dealer.hand)

    print("Player's hand:\n", '\n '.join(map(str, player.hand)))
    printBars()
    print("Dealer's hand:\n", dealer.hand[0], "\n [ HOLE CARD ]")
    printBars()

    while player.hitOrStand():
        player.hand.append(deck.deal())
        player.total = sum(card_value(card.rank) for card in player.hand)
        printBars()
        print("Player's hand:\n", ' \n '.join(map(str, player.hand)))
        printBars()
        if player.total > 21:
            print("!!!BUSTED!!! DEALER WINS.")
            return

    dealer.showHoleCard()

    
    while dealer.hitUntil17():
        dealer.hand.append(deck.deal())
        dealer.total = sum(card_value(card.rank) for card in dealer.hand)
    printBars()
    print("Dealer's hand:", ', '.join(map(str, dealer.hand)))

    print(Game.decideWinner(player.total, dealer.total))



def printBars():
    print("-----------------------------------------------------------")


if __name__ == "__main__":
    main()