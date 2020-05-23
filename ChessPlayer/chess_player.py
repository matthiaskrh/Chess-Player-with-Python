
class PlayerBase():
    def assign(self, color, board):
        self.color = color
        self.board = board

    def get_move(self):
        """
        Returns a move based on current state of board.

        Returns:
        chess.Move: Move to take
        """
        pass

