# Battleship Game

Welcome to the Battleship Game, my third project for the Code Institute's Diploma in Full Stack Software Development. This project is a digital adaptation of the classic board game Battleship, created using Python. The primary aim is to provide an engaging and interactive experience where players strategically input coordinates to target and sink their opponent's fleet.

The game runs in the Code Institute's mock terminal on Heroku.

The live link can be found here: [The Battleship Game](https://battleship-game-python-25e9a01fc0e7.herokuapp.com/).

![Battleship - Am I Responsive]()


## How to play

In the Battleship game, there are two game boards, each marked with numbers from 0 to 4, both by row and column. The player's board displays their ships as '@', and successful hits by the opponent are marked with 'X', while misses are marked with 'O'.

In this version, the player competes against the computer, with each player having a game board featuring ships placed randomly. The player attempts to guess the coordinates of the computer's ships by inputting numbers between 0 and 4 for rows and columns. 

Players take turns, and each player has 20 turns to try and hit the opponent's three ships. If a player decides to quit, they can. The objective is to strategize and sink all opponent ships before they do the same to you. 

## Site Owner Goals 

- Use the game as part of a portfolio to show what has been learned. 
- Make sure players have a great time playing the game.
- Create features that make players want to keep using the game.

## User Stories

- As a first-time user, I want clear instructions on how to input coordinates, so I can make my moves without confusion.
- As a first-time user, I want the game to be visually appealing, so it's enjoyable and easy to navigate.
- As a first-time user, I want to see both my score and the computer's score. 
- As a first-time user, I want the option to quit the game if needed, providing flexibility in my gaming experience.
- As a first-time user, I want to be able to play again when the game is over. 

## Flowchart 

To make sure I knew exactly how the game would work, I made a flowchart - kind of like a simple map for the game. This flowchart was my plan before I started building the game, and it really helped me understand how everything would fit together. 

It was super useful, especially when I needed to check if the player's input was valid. The flowchart guided me in deciding what functions to create and how these functions would work together. Even though the final game might have some differences, this flowchart was a handy tool to visualize how the game would be structured.

![Image of my flowchart]()

## Features

### Start screen 
- Battleship game logo .
- Include a welcome message and provide information about the game.
- Clearly explain how to play the game, guiding players through the rules and steps.
- Ask the player to enter their username, making them feel involved and personalizing their gaming experience.

![Screenshot of the game]()

### Game Board
  #### Battlefields
  - Set up boards for both the player and the computer for the battleship game.
  - Place ships randomly on both boards, making the game different each time.
  - Keep the computer's ships hidden, adding an element of surprise.
  - Ask the player to type in where they want to attack.
    - First, ask them to pick a row.
    - Then, ask them to pick a column.

![Board]()

### The game Score
- Keep track of whether the player or the computer successfully hit a ship or missed.
- Show the scores to let players know how well they are doing in the game.
- After each move, update the game boards to reflect the choices made by the player or the computer, making the progress visible.

![Scores]()

### Input validation
- player should choose a number only between 0 and 4!

![Invalid input]()

- Player cannot guess a coordinate twice
  
![Repeated Coordinate]()

### End of the Game
- Declare the winner of the game by making an announcement.
- Show the final scores so the player knows how they did.
- Check if the player wants to play again.
  - If they say yes, restart the game for another round.
  - If they say no, thank them for playing the game.
  
![The End]()

### Future Features
- Make the game look even better by adding more cool and colorful pictures. 
- Allow players to change things like the size of the game board, types of ships, or how hard the game is.
- Think about letting players play against their friends or other people online for more fun.

## Technologies Used
- Languages: 
  - Python
- Platform: 
  - Heroku

## Data Model  

In this game, a class named Board is created to represent the game board and manage the game's logic. Here are the key components of the data model:

### Attributes:
- `board_size`: Determines the size of the game board (set to 5 by default).
- `ship_size`: Sets the size of the ships on the board (set to 3 by default).
- `player_board` and `computer_board`: Represent the game boards for the player and computer, initialized as 5x5 grids filled with empty spaces.
- `player_turns` and `computer_turns`: Keep track of the remaining turns for each player (both set to 20 initially).
- `player_ships` and `computer_ships`: Track the remaining number of ships for each player (both set to 3 initially).

### Methods:
- `get_username()`: Prompts the user to input their username, ensuring it is at least 4 characters long.
- `display_board(board, is_player=True)`: Displays the game board. For the computer's board, it hides ships to keep them secret.
- `place_ships(board, ships)`: Randomly places ships on the board, avoiding overlap.
- `validate_input(row, col)`: Checks if the input coordinates are within the valid range of the board.
- `make_shot(board, row, col)`: Processes a player's or computer's shot on the board, updating it accordingly with "Hit" or "Miss" messages.
- `display_instructions()`: Displays comprehensive game instructions and information.
- `play_game()`: The main game loop where players take turns and outcomes are determined. It includes the logic for player and computer turns, displaying the boards, and determining the winner.
- `reset_game()`: Resets game parameters for a new round, initializing new boards and turn counts.

### Execution:
The if __name__ == "__main__": block creates an instance of the Board class and starts the game by calling the play_game() method.

## Testing 

![Screenshot of PEP8 linter]()
- The game has been tested through the [PEP8](https://pep8ci.herokuapp.com/#) linter and had no errors. 
- The players inputs have been manually tested on the Code Institute Heroku terminal and is working without any errors:
  - Invalid Username
    - Empty Character
  - Invalid Coordinates
    - A number lower than 0
    - A number higher than 4
    - A letter
    - A word
    - Empty Character

## Bugs
### Problem:
When I initially made this game, I realized that the computer's ships were not hidden. This meant that the player could easily see where the computer's ships were and hit them, which is not how the game is supposed to work. It's important for the computer's ships to be hidden so that the player has to guess where they are instead of having an unfair advantage.

### Solution:
I fixed it by one line code:

![Bug]()


## Deployment

This project was deployed using the Code Institute's mock terminal for Heroku, and the live link can be found here [The Battleship Game](https://battleship-game-python-25e9a01fc0e7.herokuapp.com/).

These steps were taken for the deployment:

- Create an account or log in to Heroku.
- On the dashboard, in the right corner click the button that says "New" and choose "Create New App".
- Pick a name of the app. The name has to be unique because it can't match any other name being used.
- Select your region, United States or Europe. 
- "Create App".
- On the menu at the top of the page, go to the Settings Tab.
- Scroll down to Config Vars and click "Reveal Config Vars".
- Add a new Config Var and enter PORT in the keybox and 8000 in the valuebox.
- Under Config Vars you will find Buildpacks. 
- Click "Add Buildpacks".
- Select python.
- Repeat this step but select nodejs. 
- Important to know: The python has to be picked before the nodejs, if it is not you can change the order by click and drag to correct the order. 
- Scroll back to the top of the page, to the menu and go to the Deploy Tab.
- Select GitHub as the deployment method and confirm. 
- Search for you repository name and connect that. 
- Scroll down to the bottom of the page and there you can choose if you want the deploys to be Automatic or Manually. The Manually deployed branches needs redepolying each time the repository is updated. 
- Click "View" to see the live site. 

## Credits

- [Love Sandwiches Project](https://github.com/tildeholmqvist/LoveSandwiches)
- [Youtube](https://www.youtube.com/watch?app=desktop&si=nCWregT0HPdC7Odt&v=alJH_c9t4zw&feature=youtu.be)
- Code Institute lessons and projects.
- My mentor Antonio for his advice and support.