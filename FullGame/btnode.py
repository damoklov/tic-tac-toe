class Node:
    """Class for representation of Node"""
    def __init__(self, item, left=None, right=None):
        """
        Constructor for class Node

        :param item: object from class Board/None
        :param left: object from class Board/None
        :param right: object from class Board/None
        """
        self.item = item
        self.left = left
        self.right = right
