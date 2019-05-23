from board import Board
from copy import deepcopy


class Game:
    def __init__(self):
        self.board = Board()

    def check_input(self, ui):
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
        if self.board.has_winner():
            return
        position = eval(position)
        self.board.make_move(position)

    def computer_make_move(self):
        if self.board.has_winner():
            return
        board1 = deepcopy(self.board)
        board1.make_random_move()
        board2 = deepcopy(self.board)
        board2.make_random_move()
        score1 = board1.compute_score()
        score2 = board2.compute_score()
        if score1 > score2:
            self.board = board1
        else:
            self.board = board2

    def launch(self):
        while not self.board.has_winner():
            pl = input('Enter move: ')
            if self.check_input(pl):
                self.player_make_move(pl)
                self.computer_make_move()
                print(self.board)
            else:
                print('Reenter correctly, please!')


if __name__ == '__main__':
    game = Game()
    game.launch()
