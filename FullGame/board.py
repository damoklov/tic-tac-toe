import random
from anytree import Node
from copy import deepcopy


def generate_winning_combinations():
    """
    Generates all possible winning combinations

    :return: list
    """
    combinations = []
    for i in range(3):
        combination1 = []
        combination2 = []
        for j in range(3):
            combination1.append((i, j))
            combination2.append((j, i))
        combinations.append(combination1)
        combinations.append(combination2)

    combinations.append([(0, 0), (1, 1), (2, 2)])
    combinations.append([(0, 2), (1, 1), (2, 0)])
    return combinations


class Board:
    """Class for representing game board"""
    NOUGHT = 1
    CROSS = -1
    EMPTY = 0

    NOUGHT_WINNER = 1
    CROSS_WINNER = -1
    DRAW = 2
    NOT_FINISHED = 0

    WINNING_COMBINATIONS = generate_winning_combinations()

    def __init__(self):
        """Constructor for class Board"""
        self.cells = [[0] * 3 for _ in range(3)]
        self.last_move = Board.NOUGHT
        self.number_of_moves = 0

    def make_move(self, cell):
        """
        Make move to a given cell

        :param cell: tuple(int, int)
        :return: bool
        """
        if self.cells[cell[0]][cell[1]] != 0:
            return False
        self.last_move = -self.last_move
        self.cells[cell[0]][cell[1]] = self.last_move
        self.number_of_moves += 1
        return True

    def has_winner(self):
        """
        Checks if there is a winner in game

        :return: int
        """
        for combination in self.WINNING_COMBINATIONS:
            lst = list()
            for cell in combination:
                lst.append(self.cells[cell[0]][cell[1]])
            if max(lst) == min(lst) and max(lst) != Board.EMPTY:
                return max(lst)
        if self.number_of_moves >= 9:
            return Board.DRAW
        return Board.NOT_FINISHED

    def make_random_move(self):
        """
        Make random move to any free cell

        :return: bool
        """
        possible_moves = list()
        for i in range(3):
            for j in range(3):
                if self.cells[i][j] == Board.EMPTY:
                    possible_moves.append((i, j))
        cell = random.choice(possible_moves)
        self.last_move = -self.last_move
        self.cells[cell[0]][cell[1]] = self.last_move
        self.number_of_moves += 1
        return True

    def compute_score(self):
        """
        Chooses better move

        :return: int
        """
        has_winner = self.has_winner()
        if has_winner:
            winner_scores = {Board.NOUGHT_WINNER: 1,
                             Board.CROSS_WINNER: -1,
                             Board.DRAW: 0}
            return winner_scores[has_winner]
        parent = Node(self)
        possible_moves = list()
        boards = list()
        for i in range(3):
            for j in range(3):
                if self.cells[i][j] == Board.EMPTY:
                    possible_moves.append((i, j))
        for _ in range(len(possible_moves)):
            boards.append(deepcopy(self))
        for b in range(len(boards)):
            boards[b].make_move(possible_moves[b])
            boards[b] = Node(boards[b], parent=parent)

        return sum([x.name.compute_score() for x in boards])

    def __str__(self):
        """String representation of game board"""
        decode = {0: " ", 1: "O", -1: "X"}
        return "\n".join(["|".join(map(lambda x: decode[x], row)) for row in self.cells])
