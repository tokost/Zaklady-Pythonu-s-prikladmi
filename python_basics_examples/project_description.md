# Tic-Tac-Toe
Create a simple tic tac toe game for two players in 3x3 grid. 
You don't need to implement the evaluation of winners. 
The game will stop after each place of the field is taken (so after 9 rounds).

## Scenario
Each round will have following scenario
1. Introduction text at the beginning of each round asking for x position: 
    ```
    Round <number of the round> player <player number either 1 or 2> turn, please specify x position.
    ```
2. Introduction text at the beginning of each round asking for y position: 
    ```
    Round <number of the round> player <player number either 1 or 2> turn, please specify y position.
    ```
3. If the specific position was already taken program will return following:
    ```
    Position [<x>, <y>] already taken please specify another position
    ```
   and the process will continue with the step 1. for the same player
4. After each run the grind will be outputed to console like 
    ```
    x - -
    - - -
    - - -
    ```
   or 
    ```
    x - -
    - o -
    - - -
    ```
5. If the game is over (after 9 rounds) the code will print: 
    ```
    Game is over thanks for playing
    ```

Use '-' symbol for free places in the grid and use dictionary for speicfication of symbols for players.
"""

## Hints 
Please use these hints only if you get lost during solving the project.
1. Specify a grid variable with nested list (watch the video nested lists)
2. Spefify a player_symbols variable with dictionary with players symbols (watch the dictionaire video)
    key = player number (either 0 or 1)
    value = symbol (either 'x', or 'o' or whatever symbol you want)
3. Create a print_grid function (watch the nested list video and hello world)
    function will receive a grid parameter and will print the array 
    dont forget to override the end parameter in print and print new line (\n) after each row.
4. Create an infinite while loop with a counter for round_number (watch the video loops)
    dont forget to increment round_number in each iteration
5. End the infinite loop in case the counter is greater or equal than 9 (because 3x3) (watch the video loops)
6. In the loop create a variable player which will have the number of the player for given round (watch the video mathematical operations )
    use the modulo operator for switching between 0 and 1 for each round.
7. Add the standard input hanling for integer
    first for x coordinate 
    then for y coordinate
8. Check in the if condition if the position in grid is free (equals to '-')

## Bonusses 
1. Add exception handling in case player specifies the position outside of the grid (like [3,3]) in this case the python should output: 
    ```
    You specified the position outside of the grid please reenter the positions. Please try again.
    ```
2. Add exception for handling cases when the player does not provide number, he provides for example string. In this case the pytho  should output: 
    ```
    You should provide only integer values as grid positions. Please try again.
    ```