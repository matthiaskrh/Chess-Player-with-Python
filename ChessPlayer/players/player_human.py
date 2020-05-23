from chess_player import PlayerBase
from chess_manager import *
import chess

class PlayerHuman(PlayerBase):
    """
    Prompts user input, sanitizes, and returns move.
    """

    def get_move(self):
        color_string = COLOR_TO_STRING[self.color]

        # Print legal moves for player reference
        print("\n\nLegal moves for " + color_string)
        for i in self.board.legal_moves:
            print(i.uci(), end=" ")

        # Input parser loop
        while(True):
            uci = input("\n\n" + color_string + ", type a move \n>")
            try:
                move = chess.Move.from_uci(uci)

                if move in self.board.legal_moves:
                    return move
                else:
                    print("Illegal move")
            except:
                print("Not recognized as a move")






