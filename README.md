# TicTacToe

## Goal
The script TTT.py trains a policy to play Tic Tac Toe.
In the game, X always moves first and O second.

## Method
The policy learns by playing against itself. This generates
a table of states which all have assigned values. Good moves
(more specifically the states associated with them) have higher
value than losing moves. The policy then chooses the best move 
based on the table it has learned. With a Q-learning algorithm 

Q(s-1) += a*(Q(s) - Q(s-1))

(where Q(x) = value of state x; s = current state, s-1 = state after last move. note that between
s-1 and s, the opponent has also made a move) 

the policy is trained by playing against itself.

## Parameters
The play_self function in TTT.py has several parameters that change
its behaviour:
-generations  ... games to be played
-agent  ...  takes a policy object to be trained(playing with 'X')
-opponent ... also takes a policy object to be trained(playing with 'O')
-prnt ... this flag can be true if you want to print out the moves
-xplr ... takes a float value that specifies the percentage of exploration moves
-init_xplr  ... takes a float value, exploration rate of the first move of a game
-learn_factor ... this is a in Q(s-1) += a*(Q(s) - Q(s-1))
-l_scale  ... if true, the learning rate scales towards 0 in linear fashion as the game count approaches generations
-xpl_scale  ... if true, the exploration rate decays (analog to l_scale)
