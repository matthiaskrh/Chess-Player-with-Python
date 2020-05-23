import chess
import time
from players import player_human, player_minimax, player_random


COLOR_TO_STRING = {chess.WHITE : "White", chess.BLACK : "Black"}


class ChessManager:
    def __init__(self, white_player, black_player):
        self.white_player = white_player
        self.black_player = black_player

        self.board = chess.Board()
        self.color_to_player = {chess.WHITE: self.white_player, chess.BLACK: self.black_player}

        white_player.assign(chess.WHITE, self.board)
        black_player.assign(chess.BLACK, self.board)

    def play(self, print_turn_info=False, delay=0):
        """
        Starts a turn by turn game with the two players.

        Parameters:
        print_turn_info (bool): Whether or not the board is printed each turn
        delay (float): Time in seconds to sleep inbetween turns

        Returns:
        (string): The result of the game when it is finished (0-1, 1-0, 1/2-1/2)
        """

        # Reset board
        self.board.reset()

        # Set initial turn
        turn = chess.WHITE

        # Game loop
        turn_count = 0
        while(True):

            current_player = self.color_to_player[turn]

            # Turn info printout
            if print_turn_info:
                print("\n\nTurn: " + str(turn_count))
                print(COLOR_TO_STRING[turn] + "'s move")
                print("Player type: " + str(type(current_player)) + "\n")
                print(self.board)

            # Getting move from player whos turn it is
            move = None
            if turn == chess.WHITE:
                move = current_player.get_move()
            elif turn == chess.BLACK:
                move = current_player.get_move()


            assert self.board.is_legal(move) # Making sure move is legal

            # Making move
            self.board.push(move)

            # Then checking if game is over
            if self.board.is_game_over():
                print("\nGame finished with final score: " + self.board.result())
                return self.board.result()

            # Update values for next turn
            turn = not turn
            turn_count += 1
            time.sleep(delay)


def tournament(rounds, w, b):
    cm = ChessManager(w, b)

    white_wins = 0
    black_wins = 0

    for i in range(rounds):
        result = cm.play(print_turn_info=False, delay=0)
        if result == "1-0":
            white_wins += 1
        elif result == "0-1":
            black_wins += 1

    print("White win percentage: " + str(100 * white_wins / (white_wins + black_wins)))
    print("Black win percentage: " + str(100 * black_wins / (white_wins + black_wins)))


if __name__ == "__main__":
    #w = player_human.PlayerHuman()
    #b = player_human.PlayerHuman()

    w = player_minimax.PlayerMinimax(2)
    b = player_minimax.PlayerMinimax(2)

    tournament(30, w, b)

