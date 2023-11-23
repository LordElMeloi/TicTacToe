import math

import random


class Player:
    #"""Base class for players in the Tic-Tac-Toe game.
    def __init__(self, letter):
        ##Initializes a new player.

        ##- letter (str): The letter representing the player ('X' or 'O').
        
        self.letter = letter

    def make_move(self, game):
       # Placeholder method for making a move in the game.

       # Parameters:
       #- game (TicTacToe): The Tic-Tac-Toe game instance.
        
        self.game = game


class RandomComputerPlayer(Player):
    #Player class representing a computer player making random moves.
    def __init__(self, letter):
        #Initializes a new random computer player.

        #Parameters:
        #- letter (str): The letter representing the player ('X' or 'O').
        
        super().__init__(letter)

    def make_move(self, game):
        #Makes a random move in the game.

        #Parameters:
        #- game (TicTacToe): The Tic-Tac-Toe game instance.

        #Returns:
        #- int: The selected tile for the move.
        tiles = random.choice(game.assessible_moves())
        return tiles


class HumanPlayer(Player):
    #Player class representing a human player making moves via user input.
    def __init__(self, letter):
        #Initializes a new human player.

        #Parameters:
        #- letter (str): The letter representing the player ('X' or 'O').
        
        super().__init__(letter)

    def make_move(self, game):
        #Takes a move from the user via input.

        #Parameters:
        #- game (TicTacToe): The Tic-Tac-Toe game instance.

        #Returns:
        #- int: The selected tile for the move.
        valid_square = False
        val = None
        while not valid_square:
            tiles = input(self.letter + '\'s turn, input move (0-8):')

            try:
                val = int(tiles)
                if val not in game.assessible_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid input, try again.')

        return val
    
class UnbeatableAiPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def make_move(self, game):
        if len(game.assessible_moves()) == 9:
            tiles = random.choice(game.assessible_moves())
        else:
            tiles = self.minimax(game, self.letter)['position']
        return tiles

    def minimax(self, game, player):
        max_player = self.letter
        other_player = 'O' if player == 'X' else 'X'

        if game.current_winner == other_player:
            return {'position': None,
                    'score': 1 * (game.num_empty_squares() + 1) if other_player == max_player else -1 *
                        (game.num_empty_squares() + 1)
                    }

        elif not game.num_empty_squares():
            return {'position': None, 'score': 0}

        if player == max_player:
            optimal = {'position': None, 'score': -math.inf}
        else:
            optimal = {'position': None, 'score': math.inf}

        for possible_move in game.assessible_moves():
            game.make_move(possible_move, player)

            sim_score = self.minimax(game, other_player)

            game.board[possible_move] = ' '
            game.current_winner = None
            sim_score['position'] = possible_move

            if player == max_player:
                if sim_score['score'] > optimal['score']:
                    optimal = sim_score
            else:
                if sim_score['score'] < optimal['score']:
                    optimal = sim_score

        return optimal

