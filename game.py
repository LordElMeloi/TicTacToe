import time

from player import HumanPlayer, RandomComputerPlayer, UnbeatableAiPlayer

class TicTacToe:
    #"""Class representing the Tic-Tac-Toe game."""

    def __init__(self):
        #"""Initializes a new Tic-Tac-Toe game."""

        self.board = [" " for _ in range(9)]
        self.current_winner = None

    def print_board(self):
       # """Prints the current state of the Tic-Tac-Toe board."""

        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_num():
        #"""Prints the board with numbers representing each tile for player reference."""
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def assessible_moves(self):
        # """Returns a list of indices representing the empty tiles on the board."""
        return [i for i, mix in enumerate(self.board) if mix == ' ']

    def empty_tiles(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, tiles, letter):
        #"""
        #Makes a move on the board.

        #Parameters:
        #- tiles (int): The selected tile for the move.
        #- letter (str): The letter representing the player making the move ('X' or 'O').

        #Returns:
        #- bool: True if the move is successful, False otherwise.
        #"""
        if self.board[tiles] == ' ':
            self.board[tiles] = letter
            if self.winner(tiles, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, tiles, letter):
        #"""
        #Checks if the current move results in a win.

        #Parameters:
        #- tiles (int): The selected tile for the move.
        #- letter (str): The letter representing the player making the move ('X' or 'O').

        #Returns:
        #- bool: True if the move results in a win, False otherwise.
        #"""
        row_ind = tiles // 3
        row = self.board[row_ind * 3: (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        col_ind = tiles % 3
        column = [self.board[col_ind + i * 3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        if tiles % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True

        return False


def play(game, x_player, o_player, print_game=True):
    #"""Prompts the user if they want to play again and returns a boolean."""
    if print_game:
        game.print_board_num()

    letter = 'X'

    while game.num_empty_squares():
        if letter == 'O':
            tiles = o_player.make_move(game)
        else:
            tiles = x_player.make_move(game)

        if game.make_move(tiles, letter):
            if print_game:
                print(letter + f' makes a move to square {tiles}')
                game.print_board()
                print(' ')

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter

            letter = 'O' if letter == 'X' else 'X'

        time.sleep(0.8)

    if print_game:
        print('It\'s a tie!')


def play_again():
    while True:
        play_again_input = input("Do you want to play again? (yes/no): ").lower()
        if play_again_input == "yes":
            return True
        elif play_again_input == "no":
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")


if __name__ == "__main__":
    while True:
        x_player = HumanPlayer('X')
        o_player = UnbeatableAiPlayer('O')
        t = TicTacToe()
        play(t, x_player, o_player, print_game=True)

        if play_again():
            # Reset the board for a new game
            t = TicTacToe()
        else:
            print("Thanks for playing! Goodbye.")
            break