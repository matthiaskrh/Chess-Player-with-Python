from chess_player import PlayerBase
import chess
import random

class PlayerRandom(PlayerBase):
    """
    Randomly chooses a move from the set of legal moves.
    """
    def get_move(self):
        legal_moves = list(self.board.legal_moves)
        return random.choice(legal_moves)