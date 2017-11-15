import random

playing = False
chip_pool = 100
count = 0
# Hearts, Diamonds,Clubs,Spades
suits = ('H','D','C','S')
# Possible card ranks
ranking = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
# Point values dict (Note: Aces can also be 11, check self.ace for details)
card_val = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10}



# Create a Card
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return self.suit + self.rank
        
    def grab_suit(self):
        return self.suit
        
    def grab_rank(self):
        return self.rank
        
    def draw(self):
        print(self.suit + self.rank)
        
        
# Create a Hand
class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        # Since Aces can be 1 or 11, set flag for later
        self.ace = False
        
    def __str__(self):
        hand_comp = ''
        
        for card in self.cards:
            card_name = card.__str__()
            hand_comp += ' ' + card_name
        
        return 'hand is: %s' %hand_comp
    
    def card_add(self, card):
        self.cards.append(card)
        
        # Check for Ace
        if card.rank == 'A':
            self.ace = True
        self.value += card_val[card.rank]
        
    def calc_val(self):
        if (self.ace == True and self.value < 12):
            return self.value + 10
        else:
            return self.value
        
    def draw(self, hidden):
        hand = []
        if hidden == True and playing == True:
            starting_card = 1
        else:
            starting_card = 0
        for x in list(range(starting_card,len(self.cards))):
            hand.append(self.cards[x].draw())
        return hand
            
            
# Create Deck
class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranking:
                self.deck.append(Card(suit, rank))
                
    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        single_card = self.deck.pop()
        return single_card
    
    def __str__(self):
        deck_comp = ''
        for card in self.cards:
            deck_comp += ' ' + card.__str__()
            
        return 'The deck has ' + deck_comp


def make_bet():
    global bet
    bet = 0
    print('Total chips:', chip_pool)
    # While loop to keep asking for the bet
    while bet == 0:
        try:
            bet = int(input('Amount of chips to bet: '))
            if 0 < bet <= chip_pool:
                break
            else:
                print('Insufficient bet:', chip_pool,'remaining.')
                bet = 0
        except:
            continue
        
        
 
def deal_cards():
    # Set up all global variables
    global result,playing,deck,player_hand,dealer_hand,chip_pool,bet,count
    
    # Create a deck
    deck = Deck()
    
    #Shuffle it
    deck.shuffle()
    
    #Set up bet
    make_bet()
    
    # Set up both player and dealer hands
    player_hand = Hand()
    dealer_hand = Hand()
    
    # Deal out initial cards
    player_hand.card_add(deck.deal())
    player_hand.card_add(deck.deal())
    
    dealer_hand.card_add(deck.deal())
    dealer_hand.card_add(deck.deal())
    
    count = 0
    playing = True
    
    game_step() 
 
 
def hit():
    global playing,chip_pool,deck,player_hand,dealer_hand,result,bet,count
    
    count = count + 1
    
    # If hand is in play add card
    if playing:
        if player_hand.calc_val() <= 21:
            player_hand.card_add(deck.deal())
        
        if player_hand.calc_val() > 21:
            result = 'Busted! '
            
            chip_pool -= bet
            playing = False
    
    else:
        result = "Sorry, can't hit" 
    
    game_step()
       
    
def stand():
    global chip_pool,deck,player_hand,dealer_hand,result,bet,playing
    
    # Soft 17 rule
    while dealer_hand.calc_val() < 17:
        dealer_hand.card_add(deck.deal())    
    
    # Dealer Busts    
    if dealer_hand.calc_val() > 21:
        print('Dealer busts! You win!')
        chip_pool += bet
        playing = False
            
    # Player has better hand than dealer
    elif dealer_hand.calc_val() < player_hand.calc_val():
        print('You beat the dealer, you win!')
        chip_pool += bet
        playing = False
        
    # Push
    elif dealer_hand.calc_val() == player_hand.calc_val():
        print('Tied up, push!')
        playing = False
        
    # Dealer beats player
    else:
        print('Dealer Wins!')
        chip_pool -= bet
        playing = False
    
    game_step()    


def natural_win():
    global result,chip_pool,playing
    result = 'You beat the dealer, you win!'
    chip_pool += bet
    playing = False
    game_step()


def natural_tie():
    global result,playing
    result = 'Tied up, push!'
    playing = False
    game_step()


def game_step():
    # Display Player Hand
    if playing == True:
        result = "Hit or Stand? Press either h or s: "
    
    print('')
    print("Player's", player_hand)
    
    print("Player's hand total is:", player_hand.calc_val())
    print('')
    
    # Display Dealer Hand
    print('Dealer hand is: '),
    dealer_hand.draw(hidden=True)
    
    # Check if player hand is 21 with a lucky Ace
    if player_hand.calc_val() == 21 and dealer_hand.calc_val() != 21 and count == 0 and playing == True:
        natural_win()
    elif player_hand.calc_val() == 21 and dealer_hand.calc_val() == 21 and count == 0 and playing == True:
        natural_tie()
    else:
        # Print result of hit or stand.
        print('')
        # If game round is over
        if playing == False:
            result = "Enter D, or Q: "
            print("Dealer's hand total:", dealer_hand.calc_val())
            print('Chip Total:', chip_pool)
            player_input(result)
        else:
            player_input(result)


def player_input(result):
    choice = input(result).lower()
    
    if choice == 'h':
        hit()
    elif choice == 's':
        stand()
    elif choice == 'd':
        deal_cards()
    elif choice == 'q':
        blackjack_exit()
    else:
        print("Invalid Input...Enter H, S, D, or Q: ")
        player_input()
      
        
def blackjack_exit():
    print('Thank you for playing!')
    exit()
 
while True:
    print('Welcome to Blackjack!')
    # Create a Deck
    #deck = Deck()
    #Shuffle it
    #deck.shuffle()
    
    # Create player and dealer hands
    #player_hand = Hand()
    #dealer_hand = Hand()
    
    # Deal out the cards and start the game!
    deal_cards()
    




