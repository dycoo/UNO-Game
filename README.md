# UNO Card Game

This is a Python implementation of the UNO card game. The game allows multiple players to play UNO by matching cards based on color or number.

## Classes

### `player`
Represents a player in the game.
- `__init__(self, name)`: Initializes a player with a name.
- `setup_initial_cards(self, deck)`: Sets up initial cards for the player.
- `add_card(self, in_card)`: Adds a card to the player's hand.
- `add_cards(self, in_cards)`: Adds multiple cards to the player's hand.
- `get_cards(self)`: Returns the player's cards.
- `get_name(self)`: Returns the player's name.
- `__str__(self)`: Returns a string representation of the player.

### `deck`
Represents the deck of cards.
- `__init__(self)`: Initializes the deck.
- `load_deck(self)`: Loads the deck with cards.
- `display_deck(self)`: Displays the deck.
- `shuffle_deck(self)`: Shuffles the deck.
- `get_cards_number(self)`: Returns the number of cards in the deck.
- `pull_cards(self, num_of_cards=1)`: Pulls a specified number of cards from the deck.
- `__str__(self)`: Returns a string representation of the deck.

### `game`
Represents the game.
- `__init__(self, deck)`: Initializes the game with a deck.
- `show_table_card(self)`: Shows the current table card.
- `show_players_cards(self)`: Shows the cards of all players.
- `request_players_names()`: Requests the names of the players.
- `set_players(self, players)`: Sets the players for the game.
- `display_players(self)`: Displays the players.
- `start_the_game(self)`: Starts the game.
- `__str__(self)`: Returns a string representation of the game.

### `main()`
The main function to initialize and start the game.

## Activity Flow Diagram

```mermaid
graph TD
    A[Start Game] --> B[Initialize Deck]
    B --> C[Load Deck]
    C --> D[Shuffle Deck]
    D --> E[Request Player Names]
    E --> F[Set Players]
    F --> G[Setup Initial Cards for Players]
    G --> H[Display Players]
    H --> I[Start the Game]
    I --> J[Player Turn]
    J --> K{Card Matches Table Card?}
    K --> |Yes| L[Play Card]
    K --> |No| M[Try Again]
    L --> N{Player Has One Card?}
    N --> |Yes| O[Shout UNO]
    N --> |No| P[Next Player Turn]
    O --> P
    P --> Q{Player Has No Cards?}
    Q --> |Yes| R[Declare Winner]
    Q --> |No| J
    R --> S[End Game]
