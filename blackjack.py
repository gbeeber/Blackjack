import random
class Player():
    """This class keeps track of all of the players"""

    def __init__(self, name, balance=500):
        self.name = name
        self.balance = balance

    def __str__(self):
        return f"{self.name}'s balance is {self.balance}"

def player_won(self,bet):
    self.balance += bet
    print(f'\nCongratulations!  You won {bet} and your new balance is {self.balance}\n')

def player_lost(self,bet):
    self.balance -= bet
    print(f'\nToo bad!  You lost {bet}. Your new balance is {self.balance}\n')

class Card():

    def __init__(self, suit, number, value):
        self.suit=suit
        self.number=number
        self.value=value

    def __str__(self):
        return f'{self.number} of {self.suit}'

# Checks value of the hand.  If the hand is greater than 21 and there is an ace,
# it sends back the new hand_total.
def value_of_hand(cards):
    hand_total=0
    ace=False
    for i in range(0,len(cards)):
        hand_total+=cards[i].value
        if cards[i].number=='A':
            ace=True
    if hand_total > 21 and ace==True:
        hand_total-=10
    return hand_total

def deal_card(deck,dealer_cards,player_cards):
    newcard=Card('blank','blank',0)
    while newcard.suit=='blank' or newcard in dealer_cards or newcard in player_cards:
        r=random.randint(1,52)
        newcard=deck[r-1]
    return newcard

def gameover(person):
    while True:
        print(f'Your balance is {person.balance}.')
        again=input(f'{person.name}, would you like to play again (Y or N)? ')
        if again == 'y' or again == 'Y':
            return True
        elif again == 'n' or again == 'N':
            quit()
            return False
        else:
            print('Bad input.  Please only enter a "Y" or "N".')

def ask_hit():
    while True:
        hitinput=input(f'\n{person.name}, would you like to hit (Y or N)? ')
        if hitinput == 'y' or hitinput == 'Y':
            return True
        elif hitinput == 'n' or hitinput == 'N':
            return False
        else:
            print('Bad input.  Please only enter a "Y" or "N".')

def print_cards(dealer_cards,player_cards,recap):
    print('\n'*100)
    if recap==False:
        print(f"\nThe dealer's card is {dealer_cards[0]}\n")
    else:
        print("\nThe dealer's cards are: ")
        for i in range(0,len(dealer_cards)):
            print(dealer_cards[i])
    print('\nYour cards are:')
    for i in range(0,len(player_cards)):
        print(player_cards[i])

# Populate the deck first with hearts, diamonds, spades, and clubs in order
h=[]
d=[]
s=[]
c=[]
deck=[]
r=range(2,11)
face={'J':10,'Q':10,'K':10,'A':11}

for i in r:
    h.append(Card('Hearts', str(i), i))
    d.append(Card('Diamonds', str(i), i))
    s.append(Card('Spades', str(i), i))
    c.append(Card('Clubs', str(i), i))
for k,v in face.items():
    h.append(Card('Hearts', k, v))
    d.append(Card('Diamonds', k, v))
    s.append(Card('Spades', k, v))
    c.append(Card('Clubs', k, v))
for i in range(0,13):
    deck.append(h[i])
    deck.append(d[i])
    deck.append(s[i])
    deck.append(c[i])

# Find out the person's name
name=input('Please enter your name:  ')
person=Player(name)

# Start the game
keepplaying=True
while keepplaying==True:
    startover=False
    # Find out how much the player wants to bet
    dealer_cards=[]
    player_cards=[]
    for i in range(0,len(dealer_cards)):
        dealer_cards.pop(0)
    for i in range(0,len(player_cards)):
        player_cards.pop(0)
    print('\n'*2)
    print(person)
    print('\n')
    while True:
        try:
            bet=int(input(f'{person.name}, how much would you like to bet?  '))
            if bet > person.balance:
                print(f'Your bet is too high.  You can only bet up to {person.balance}\n')
                continue
            break
        except:
            print('Bad input.  Please enter an integer only\n')

    # Deal the cards
    for i in range(0,2):
        newcard=deal_card(deck,dealer_cards,player_cards)
        dealer_cards.append(newcard)
    for i in range(0,2):
        newcard=deal_card(deck,dealer_cards,player_cards)
        player_cards.append(newcard)
    print_cards(dealer_cards,player_cards,False)
    if value_of_hand(player_cards) == 21 and value_of_hand(dealer_cards) != 21:
        print('You got a blackjack!')
        player_won(person,bet)
        keepplaying=gameover(person)
        startover=keepplaying
    elif value_of_hand(player_cards) != 21 and value_of_hand(dealer_cards) == 21:
        print('The dealer has blackjack!')
        player_lost(person,bet)
        keepplaying=gameover(person)
        startover=keepplaying
    elif value_of_hand(player_cards) == 21 and value_of_hand(dealer_cards) == 21:
        print('Push!')
        keepplaying=gameover(person)
        startover=keepplaying
    if startover==True:
        continue
    # Ask for hit or stay
    hit=True
    while hit==True:
        hit=ask_hit()
        if hit==True:
            newcard=deal_card(deck,dealer_cards,player_cards)
            player_cards.append(newcard)
            print_cards(dealer_cards,player_cards,False)
            if value_of_hand(player_cards) > 21:
                print('You busted!')
                player_lost(person,bet)
                keepplaying=gameover(person)
                startover=keepplaying
                hit=False
    if startover==True:
        continue
    # Dealer's turn
    dealerhit=True
    while dealerhit==True:
        if value_of_hand(dealer_cards) < value_of_hand(player_cards) or value_of_hand(dealer_cards)<=16:
            newcard=deal_card(deck,dealer_cards,player_cards)
            dealer_cards.append(newcard)
        else:
            dealerhit=False
    print_cards(dealer_cards,player_cards,True)
    print(f"\nThe value of the dealer's hand is {value_of_hand(dealer_cards)}")
    print(f"The value of the player's hand is {value_of_hand(player_cards)}")

    # Check the results
    if value_of_hand(dealer_cards) > value_of_hand(player_cards) and value_of_hand(dealer_cards) <= 21:
        player_lost(person,bet)
        keepplaying=gameover(person)
        continue
    if value_of_hand(dealer_cards) == value_of_hand(player_cards):
        print('Push!')
        keepplaying=gameover(person)
        continue
    else:
        player_won(person,bet)
        keepplaying=gameover(person)
