#This a UNO cardboard game code

import random

class player:
    def __init__(self, name):
        self.name = name
        self.num_card=0
        self.uno=False
        self.cards = []


    def setup_initial_cards(self, deck):
        #print(deck.pull_cards(7))
        self.cards = deck.pull_cards(7)
        self.num_card = 7



    def add_card(self, in_card):
        self.cards.append(in_card)
        self.num_card+=1
        self.uno=False

    def add_cards(self, in_cards):
        self.cards.extend(in_cards)    
        self.num_card+=len(in_cards)
        self.uno=False


    def get_cards(self):
        return self.cards   
    
    
    def get_name(self):
        return self.name

    def __str__(self):
        return f'{self.name} has {self.num_card} cards'

class deck:
    def __init__(self):
        self.cards = []

    def load_deck(self):
        temp_colors = ['red', 'blue', 'green', 'yellow']
        temp_values = ['0','1','2','3','4','5','6','7','8','9']
        temp_wilds = ['wild','draw4','skip','reverse','draw2']
        
        for i in range(3):
            for color in temp_colors:
                for value in temp_values:
                    self.cards.append(f'{color} {value}')

    #display the deck
    def display_deck(self):
        print(self.cards)   


    #shuffle the deck
    def shuffle_deck(self):
        random.shuffle(self.cards)

    #get number of cards in the deck
    def get_cards_number(self):
        return len(self.cards)

    #pull cards from the deck    
    def pull_cards(self, num_of_cards=1 ):
        
        temp_cards = []
        
        #check if there are enough cards in the deck
        if self.get_cards_number()<num_of_cards:
            print('Not enough cards in deck, let me shuffle the deck')
            #load the deck
            self.load_deck()

            #shuffle the deck
            self.shuffle_deck()   
        
        #get the cards from the deck
        for i in range(num_of_cards):
            temp_cards.append(self.cards.pop()) 
        
        return temp_cards

    def __str__(self):
        return f'Deck has {len(self.cards)} cards'

class game:
    def __init__(self, deck):
        self.players = []
        self.deck = deck
        self.table_card = ""


    def show_table_card(self):
        print(f'Table card is {self.table_card}')   

    #show the cards of the players
    def show_players_cards(self):     
        for player in self.players:
            print(player.get_name())
            print(player.get_cards())
            
    
    # request the number and name of the players
    def request_players_names():
        temp_players = []
        num_of_players = int(input('Enter number of players: '))
        for i in range(num_of_players):
            name = input(f'Enter player {i+1} name: ')
            temp_players.append(player(name))
        return temp_players

    #setup the players to the game
    def set_players(self, players):
        self.players = players
    
    
    #display the players
    def display_players(self):   
        
        print("These are the players: ")
        for player in self.players:
            print(player)
        


    def start_the_game(self):   
        
        #setup initial table card
        self.table_card = self.deck.pull_cards(1)[0]
        print(f'Table card is {self.table_card}')   
        
        #request the players to trow a card that match the table card until we have a winner with no cards
        winner = False
        while not winner:
            for player in self.players:
                print(f'{player.get_name()} turn')
                print(player.get_cards())
                card = input('Enter the card you want to play: ')
                if card in player.get_cards():
                    if card.split()[0] in self.table_card.split()[0] or card.split()[1] in self.table_card.split()[1]:
                        print(f'{player.get_name()} played {card}')
                        player.cards.remove(card)
                        self.table_card = card
                        print(f'New table card is {self.table_card}')
                    else:
                        print('You can not play that card, try again')
                        continue
                    
                    
                    if len(player.get_cards())==1:
                        print('UNO')
                        player.uno=True
                    
                    if len(player.get_cards())==0:
                        winner = True
                        print(f'{player.get_name()} is the winner')
                        break
                else:
                    print('You dont have that card, try again')
                    continue
        

    def __str__(self):
        return f'Game has {len(self.players)} players and {len(self.deck.cards)} cards reminding in the deck'


def main():

    #deck initialization
    d = deck()
    d.load_deck()
    d.shuffle_deck()
    #d.display_deck()

    #game initialization
    g = game(d)
    
    #request the players names
    g.set_players(game.request_players_names())

    
    #setup the initial cards for each player    
    for player in g.players:
        player.setup_initial_cards(d)  
    
    #print(g)

    #display the players
    g.display_players() 

    # g.show_players_cards()

    g.start_the_game()


main()