import chess
import time
from players import player_human, player_minimax, player_random


COLOR_TO_STRING = {chess.WHITE : "White", chess.BLACK : "Black"}


class ChessManager:
    def __init__(self, white_player, black_player):
        self.board = chess.Board()
        self.white_player = white_player
        self.black_player = black_player
        self.color_to_player = {chess.WHITE: self.white_player, chess.BLACK: self.black_player}

        white_player.assign(chess.WHITE, self.board)
        black_player.assign(chess.BLACK, self.board)

    def play(self, is_displayed=False, delay=0):
        """
        Starts a turn by turn game with the two players.

        Parameters:
        is_displayed (bool): Whether or not the board is printed each turn
        delay (float): Time in seconds to sleep inbetween turns
        """

        # Set initial turn
        turn = chess.WHITE

        # Game loop
        turn_count = 0
        while(True):

            current_player = self.color_to_player[turn]

            if is_displayed:
                print("\n\nTurn: " + str(turn_count))
                print(COLOR_TO_STRING[turn] + "'s move")
                print("Player type: " + str(type(current_player)) + "\n")
                print(self.board)

            move = None
            if turn == chess.WHITE:
                move = current_player.get_move()
            elif turn == chess.BLACK:
                move = current_player.get_move()

            assert self.board.is_legal(move)

            self.board.push(move)

            if self.board.is_game_over():
                print("\nGame finished with final score: " + self.board.result())
                break

            turn = not turn
            turn_count += 1

            time.sleep(delay)




if __name__ == "__main__":
    #w = player_human.PlayerHuman()
    #b = player_human.PlayerHuman()

    b = player_minimax.PlayerMinimax(2, print_move_info=True)
    w = player_random.PlayerRandom()

    cm = ChessManager(w, b)
    cm.play(is_displayed=True, delay=0)