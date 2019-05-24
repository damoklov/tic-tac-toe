from board import Board
from copy import deepcopy


class Game:
    """Class for representation of a Tic-Tac-Toe game"""
    def __init__(self):
        """Constructor for class Game"""
        self.board = Board()

    def check_input(self, ui):
        """
        Checks user input for errors

        :param ui: str
        :return: bool
        """
        try:
            ui = eval(ui)
            if not (isinstance(ui, tuple) or isinstance(ui, list)):
                raise TypeError
            elif not (isinstance(ui[0], int) and isinstance(ui[1], int)):
                raise TypeError
            elif len(ui) != 2:
                raise Exception
            elif self.board.cells[ui[0]][ui[1]] != Board.EMPTY:
                raise Exception
            else:
                assert 0 <= ui[0] <= 2
                assert 0 <= ui[1] <= 2
        except (AssertionError, TypeError, NameError, SyntaxError, Exception):
            return 0
        else:
            return 1

    def player_make_move(self, position):
        """
        Makes move for player

        :param position: tuple(int, int)
        :return: None
        """
        if self.board.has_winner():
            return
        position = eval(position)
        self.board.make_move(position)

    def computer_make_move(self):
        """
        Makes move for AI

        :return: None
        """
        if self.board.has_winner():
            return
        possible_moves = list()
        boards = list()
        for i in range(3):
            for j in range(3):
                if self.board.cells[i][j] == Board.EMPTY:
                    possible_moves.append((i, j))
        for _ in range(len(possible_moves)):
            boards.append(deepcopy(self.board))
        for b in range(len(boards)):
            boards[b].make_move(possible_moves[b])
        max_score_board = max(boards, key=lambda x: x.compute_score())
        self.board = max_score_board

    @staticmethod
    def get_winner(code):
        """
        Decodes winner

        :param code: int
        :return: str
        """
        decoder = {1: 'AI won!', -1: 'User won!', 0: 'Draw.'}
        return decoder[code]

    def launch(self):
        """
        Launches main game loop

        :return: None
        """
        while not self.board.has_winner():
            pl = input('Enter move: ')
            if self.check_input(pl):
                self.player_make_move(pl)
                self.computer_make_move()
                print(self.board, end='\n\n')
            else:
                print('Reenter correctly, please!')
        print(self.get_winner(self.board.has_winner()))


if __name__ == '__main__':
    game = Game()
    game.launch()
