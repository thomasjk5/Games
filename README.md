# Tictactoe
The program starts by asking the player 1’s name and stored to p1 followed by player 2’s name being stored in p2.
The player 1 can choose between X and O.If the player 1 selected X and variable player turn is ini6alled to 1 and 
if the player select O player turn is ini6alised to 0,Then p1,p2 is swapped.
The game starts and the 6c tac toe is printed in 3X3 format using a func6on called printg() .
A variable called end is ini6alised to 1.
A while loop with condi6on end is started.
The player 1 can choose the posi6on number aWer player 1 entered the posi6on number the playerturn value is changed to O if t
he player 1 chose X before and playerturn changed to X if player 1 chose O first.
The win condi6ons are checked using if condi6ons which check rows , columns and diagonally.If the condi6on is true 
the end value is changed to 0 and while loop is exited.
And if the game ends in a draw the entires are counted and if the count is 9 the count is incremented by 1.
The count becomes 10, and while loop is exited.
Outside the loop all condi6ons are checked if count is 10, the result is printed “The game ends in a Tie”
If the playerturn is 0 the result is printed “Player 1 wins!”
if the playerturn is 1 the result is “ player 2 wins!” .
