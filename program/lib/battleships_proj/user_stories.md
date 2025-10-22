## User Stories

---
# Notes on application
Battleship is a 10x10 square
5 Ships:
    Carrier 5x1
    Battleship 4x1
    Destroyer 3x1
    Submarine 3x1
    Patrol boat 2x1
42 Red pegs
84 White Pegs

### Classes:
    Board
        Yours
        Opponents
    Ship
        {each ship}
    Pegs
        Red
        White

### Representation
    Each point per board will be a dictionary value
        key: 1a, 1b, 1c etc
        value: [ship: state]
            Another nested dictionary - used to hold additional data about the ships location - will link occupied values on the board to a ship piece
            pin_location[1][1] - retrieves state
                state: Nonne, 'Hit', 'Miss', 'Sunk', 'Occupied'
                Values will be retrieved differently depending on the function (eg. display board, place ship, fire at ship)
            ship_type[1][0] - retrives ship details
                type: Carrier, Battleship , Destroyer, Submarine, Patrol Boat

        [position: [ship_type, state]]

        missed example: '1a': [None, 'Miss']
        hit example: '2b': ['Destroyer', 'Hit']

    Printout to console for visual representation
        - - - - x - o - x x
        - - - - x - - o - -
        x: hit, o: miss, S: occupied, #: sunk, -: None


### Functionality
    Should be split into game phases:
        1. Setup phase
            - Players place ships on their board
        2. Play phase
            - Players take turns firing at each other's boards
        3. End phase
            - Game ends when one player sinks all opponent's ships

    Global variable to track game state:
        game_phase = 'setup' / 'play' / 'end'
    
    Global variable to track current player:
        current_player = 'player1' / 'player2'
        # Switch after each turn in play phase - prevents same player going twice or affecting opponent's board

    # AI opponent or human opponent?
        What would be the best way to implement this?
        - If AI opponent, create a simple algorithm for ship placement and firing
        - If human opponent, need to manage input for both players without revealing ship positions
            - Seperation of print functions. One for your board, one for opponent's board (hides ship positions) for AI opponent.
            - For human opponent, display evenly for both. Assume honour system

    - Priority:
        E - Essential, H - High, M - Medium, L - Low, N - Non-essential

    Core features to be implemented (Requiring additional thought/planning):
        E - Two-player mode (local) / AI opponent -> outcome based on above comment

    Time consuming or tasking features (to be added later if time permits):
    # Doesnt detract from core gameplay, but would enhance user experience
        L - Implement end phase display
        L - Implement end phase navigation (play again, exit)
        M - Delete or replace ships during setup phase
        M - Prompt to end turn during play phase
        M - Print remaining ships to place during setup phase

        N - Score tracking across multiple games
        N - Save/load game state

##### Setup phase functionality:
    - Place ship at specified location
    - Validate ship placement (within bounds, no overlap) - validating hidden function
    - Choose ship orientation (up, down, left, right) - parameter for placement function

    Ship placement logic:
        - Check if ship fits in the desired location
        - Update board state with ship positions
        Function should select a pin location and either up, down, left or right from that position based on user input. The relative ship data should be retrieved from a ship class to determine how many spaces to fill on the board.

        example implementation:
            place_ship(your_board, 'Destroyer', '3c', 'right')
    
        def place_ship(board, ship, start_pos, direction):
            # Logic to place ship on board at specified location and direction

        def validate_placement(board, ship, start_pos, direction):
            # Logic to validate ship placement - Check bounds and overlap
            # Function used as check before placing ship
            return True or False
        

##### Play phase functionality:
###### Display boards
    example implementation:
            display_ships(your_board)

    def display_ships(board, player):
    # Show player's own board with ship positions and hits/misses
        # If local play, prints appropriate board - requires parameter to identify player

        if player != current_player:
            return  # Prevents opponent from seeing your ships

        for position, data in board.items():
            listed_ships = []
            if data[0] is not None:
                listed_ships.append(f"{data[0]} at {position}")
                # Sort and display ships
                listed_ships.sort()
        print(f"Your ships: {listed_ships}")
        # Seperate from below function - shows only positions, no action data

    def print_board(board, player):
    # Prints the board to the console - params are board type (yours/opponents, current player)
        if board_type == 'yours':
        # Variable yours refers directly to global current_player
        # Only prints the current player with all details, else prints opponent board with limited details
            print("Your Board:")
            for row in range(1, 11):
                row_display = ""
                for col in 'abcdefghij':
                    pos = f"{row}{col}"
                    state = board[pos][1]
                    if state == 'Hit':
                        row_display += " x "
                    elif state == 'Miss':
                        row_display += " o "
                    elif state == 'Occupied':
                        row_display += " S "
                    elif state is 'Sunk':
                        row_display += " # "
                    else:
                        row_display += " - "
                print(row_display)
        elif board_type == 'opponents':
            print("Opponent's Board:")
            for row in range(1, 11):
                row_display = ""
                for col in 'abcdefghij':
                    pos = f"{row}{col}"
                    state = board[pos][1]
                    if state == 'Hit':
                        row_display += " x "
                    elif state == 'Miss':
                        row_display += " o "
                    else:
                        row_display += " - "
                print(row_display)

###### Input functionality



---
**As a player**  
So that I can prepare for the game  
I would like to place a ship in a board location.


---

**As a player**  
So that I can play a more interesting game  
I would like to have a range of ship sizes to choose from.

---

**As a player**  
So the game is more fun to play  
I would like a nice command line interface that lets me enter ship positions and shots using commands.

---

**As a player**  
So that I can create a layout of ships to outwit my opponent  
I would like to be able to choose the directions my ships face in.

---

**As a player**  
So that I can have a coherent game  
I would like ships to be constrained to be on the board.

---

**As a player**  
So that I can have a coherent game  
I would like ships to be constrained not to overlap.

---

**As a player**  
So that I can win the game  
I would like to be able to fire at my opponent's board.

---

**As a player**  
So that I can refine my strategy  
I would like to know when I have sunk an opponent's ship.

---

**As a player**  
So that I know when to finish playing  
I would like to know when I have won or lost.

---

**As a player**  
So that I can consider my next shot  
I would like to be able to see my hits and misses so far.

---

**As a player**  
So that I can play against a human opponent  
I would like to play a two-player game.

---