# Python Chess Player

Create a new ChessManager to start a game.


## Implemented Players:

Human controlled - When asked for a move prompts player input

Random - Randomly selected move from list of legal moves

Minimax - Uses a limited depth minimax search with alpha-beta pruning to get optimal move


## Sample Code:

This is how you run a simple human vs computer game:
```
import chess_manager
from players import player_human, player_minimax

w = player_human.PlayerHuman()
b = player_minimax.PlayerMinimax(2, print_move_info=True) # 2 is the depth of the search tree

cm = ChessManager(w, b)
cm.play(is_displayed=True, delay=0)
```


And here is a computer vs computer game:
```
import chess_manager
from players import player_minimax
 
w = player_minimax.PlayerMinimax(2, print_move_info=True) # 2 is the depth of the search tree
b = player_minimax.PlayerMinimax(2, print_move_info=True) # 2 is the depth of the search tree

cm = ChessManager(w, b)
cm.play(is_displayed=True, delay=0)
```



Lastly, computer vs random move generator:
```
import chess_manager
from players import player_minimax, player_random

w = player_minimax.PlayerMinimax(2, print_move_info=True) # 2 is the depth of the search tree
b = player_random.PlayerRandom()

cm = ChessManager(w, b)
cm.play(is_displayed=True, delay=0)
```



## Dependency

python-chess https://pypi.org/project/python-chess/
