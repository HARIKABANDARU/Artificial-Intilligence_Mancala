# Artificial-Intilligence_Mancala
An AI game implemented with two AI algorithms
This project is or mancala game.
Mancala is played with a board that contains a number of positions, as shown in Fig. 4. The
large positions on left and right are called “mancalas.”
Rules : Implemented for this project are :
 "" Each position can contain 0 or more stones. In each turn, a player picks up all stones
from one position and then deposits the stones one at a time in subsequent positions, moving
counter-clockwise around the board, until no stones are left in their hand. Each player wants
to maximize the number of stones in their own mancala (on their right) and minimize the
number of stones in the opponent’s mancala (on their left). Each player can pick up only
from the small positions on their half of the board, and skips the opponent’s mancala when
depositing stones. If the last stone in a player’s hand is deposited in an empty small position
on their half of the board, they get to move that stone to their mancala, as well as any stones in
the adjacent small position on the opponent’s side of the board. If the last stone in a player’s
hand is deposited in their own mancala, they get to go again, skipping the opponent’s turn.
Gameplay ends once a player has cleared all stones on their half of the board. At that point,
the opponent gets to move all of the remaining stones on the opponent’s half of the board
to the opponent’s mancala. A player’s score at any turn is number of stones in their own
mancala, minus the number of stones in the opponent’s mancala. The winner is the player
with the highest score after the last turn.""

See the image mancalaBoard.png for visualisation of how board looks like.

It was played by three different ways:
  1 Normal game.
  2 Using minmax algorithm
  3 Using minmax with alpha-beta pruning.
  
   
