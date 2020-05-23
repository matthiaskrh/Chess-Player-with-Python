from chess_player import PlayerBase
import chess_manager
import chess
import random
import time


class PlayerMinimax(PlayerBase):
    """
    Player that searches a minimax tree of limited depth for the best possible move to make.
    """
    def __init__(self, max_depth, is_debug=False):
        self.max_depth = max_depth
        self.is_debug = is_debug


    def get_move(self):

        init_time = time.time()

        # Create a test board seperate from real board to minimax search on
        test_board = self.board.copy()

        best_score, best_move = self.score_tree_with_ab(test_board, float("-inf"), float("inf"), 0)
        #best_score, best_move = self.score_tree(test_board, 0)

        if self.is_debug:
            print("Took "
                  + str(time.time() - init_time)
                  + " to get move "
                  + str(best_move)
                  + " with score "
                  + str(best_score))


        return best_move


    def score_tree_with_ab(self, board, a, b, depth):
        """ Recusive function that depth searches the game tree of a chess board and uses alpha beta pruning

        :param board: board on which to depth search on
        :type board: chess.Board

        :param a: alpha for alpha-beta pruning
        :type a: float

        :param a: beta for alpha-beta pruning
        :type a: float

        :param depth: max recursion depth to search
        :type depth: int

        :return: Best possible score and the next move towards it
        :rtype: 2-tuple (int, chess.Move)
        """

        # Recursion limit
        if depth >= self.max_depth:
            return self.get_board_score(board), None

        # Check if game is over
        if board.is_game_over():
            # Case 1: White wins
            if board.result() == "1-0":
                if self.color == chess.WHITE:
                    end_score = float("inf")
                else:
                    end_score = float("-inf")
            # Case 2: Black wins
            elif board.result() == "0-1":
                if self.color == chess.WHITE:
                    end_score = float("-inf")
                else:
                    end_score = float("inf")
            # Case 3: Tie
            else:
                end_score = 0

            return end_score, None


        # Creating list of legal moves and shuffling it so moves are not repeated
        legal_moves = list(board.legal_moves)
        random.shuffle(legal_moves)

        # If maximizing player
        if board.turn == self.color:
            value = float("-inf")
            move = None

            for i in legal_moves:
                board.push(i)
                r = self.score_tree_with_ab(board, a, b, depth + 1)

                if r[0] > value:
                    value = r[0]
                    move = i

                a = max(a, value)

                assert i == board.peek()
                board.pop()

                if a >= b:
                    break

            return (value, move)

        # If minimizing player
        else:
            value = float("inf")
            move = None

            for i in legal_moves:
                board.push(i)
                r = self.score_tree_with_ab(board, a, b, depth + 1)

                if r[0] < value:
                    value = r[0]
                    move = i

                b = min(b, value)

                assert i == board.peek()
                board.pop()

                if a >= b:
                    break

            return (value, move)


    def score_tree(self, board, depth):
        """ Recusive function that depth searches the game tree of a chess board.

        :param board: board on which to depth search on
        :type board: chess.Board

        :param depth: max recursion depth to search
        :type depth: int

        :return: Best possible score and the next move towards it
        :rtype: 2-tuple (int, chess.Move)
        """

        # Recursion limit
        if depth >= self.max_depth:
            return self.get_board_score(board), None

        # Check if game is over
        if board.is_game_over():
            # Case 1: White wins
            if board.result() == "1-0":
                if self.color == chess.WHITE:
                    end_score = float("inf")
                else:
                    end_score = float("-inf")
            # Case 2: Black wins
            elif board.result() == "0-1":
                if self.color == chess.WHITE:
                    end_score = float("-inf")
                else:
                    end_score = float("inf")
            # Case 3: Tie
            else:
                end_score = 0

            return end_score, None


        # If not terminal state, then search all possible moves from here
        child_scores = []
        score_to_move = {}

        # Creating list of legal moves and shuffling it so moves are not repeated
        legal_moves = list(board.legal_moves)
        random.shuffle(legal_moves)

        for i in legal_moves:
            board.push(i)

            r = self.score_tree(board, depth + 1)
            child_scores.append(r[0])
            score_to_move[r[0]] = i

            assert i == board.peek()
            board.pop()

        # If it is our turn, maximize
        if board.turn == self.color:
            node_score = max(child_scores)
        # If opponent's turn, minimize
        else:
            node_score = min(child_scores)


        # DEBUG
        if depth == 0:
            assert board.turn == self.color

        if node_score < 0 and depth == 0:
            print(node_score, score_to_move, child_scores)
        #DEBUG


        return (node_score, score_to_move[node_score])


    def get_piece_score(self, piece):
        """
        Calculates score of a single piece based on its position on the board, how many attackers it has, how many
        pieces its attacking, and its type.

        Parameters:
        piece (chess.Piece): Piece to get score of

        Returns:
        int: Score of piece
        """

        if piece.color == self.color:
            if piece.piece_type == chess.PAWN:
                return 1
            if piece.piece_type == chess.KNIGHT:
                return 3
            if piece.piece_type == chess.BISHOP:
                return 3
            if piece.piece_type == chess.ROOK:
                return 5
            if piece.piece_type == chess.QUEEN:
                return 9
            if piece.piece_type == chess.KING:
                return 0
        else:
            return 0


    def get_board_score(self, board):
        """
        Sums up score of all pieces on the board and returns that value.

        Parameters:
        board (chess.Board): Board to get the score of

        Returns:
        int: Score of board
        """

        score = 0
        pieces = board.piece_map()
        for i in pieces.keys():
            score += self.get_piece_score(pieces[i])
        return score



