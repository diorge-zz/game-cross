from enum import Enum


BOARD_SIZE = 9


class TroopType(Enum):
    Swordsman = 1
    Spearman = 2
    Archer = 3
    Horseman = 4
    General = 5


class Color(Enum):
    Black = 0
    White = 1


STARTING_BOARD = [[
            TroopType.Spearman, TroopType.Swordsman, TroopType.Swordsman,
            TroopType.Horseman, TroopType.General, TroopType.Horseman,
            TroopType.Swordsman, TroopType.Swordsman, TroopType.Spearman
        ], [
            TroopType.Spearman, TroopType.Spearman, TroopType.Swordsman,
            TroopType.Archer, TroopType.Archer, TroopType.Archer,
            TroopType.Swordsman, TroopType.Spearman, TroopType.Spearman
        ]]


class Piece(object):
    """ Piece on the board """

    def __init__(self, trooptype, color):
        """ Instantiates a new piece"""
        self.trooptype = trooptype
        self.color = color

    def __eq__(self, other):
        """ Equality between pieces """
        if other is None:
            return False
        return (self.trooptype, self.color) == (other.trooptype, other.color)


class Position(object):
    """ A position on the board """

    def __init__(self, h, v):
        """
        Creates a new position for (H, V)
        Note H is in range [1, 9] and V is in range [A, I] (uppercase)
        """
        self._h = h
        self._v = v
        vidx = ord(v) - ord('A')
        self._idx = vidx * BOARD_SIZE + (h - 1)

    @property
    def index(self):
        """ Returns the [0, 80] index of the position """
        return self._idx

    @staticmethod
    def parse(s):
        """ Parses a position string to a position object """
        if len(s) != 2:
            raise ValueError('Invalid position: ' + s)
        n = int(s[0])
        c = s[1]
        if 1 <= n <= 9 and ord('A') <= ord(c) <= ord('I'):
            return Position(n, c)
        raise ValueError('Invalid position ' + s)


class Board(object):
    """ Abstract board representation """

    def __init__(self):
        """ Creates an empty board """
        self.pieces = [None] * (BOARD_SIZE * BOARD_SIZE)

    def __getitem__(self, pos):
        """ Returns the piece in the given position """
        return self.pieces[pos.index]

    def __setitem__(self, pos, piece):
        """ Puts a piece in a given position """
        self.pieces[pos.index] = piece

    def __delitem(self, pos):
        """ Removes a piece from the board """
        self.pieces[pos.index] = None

    def __eq__(self, other):
        """ Compares two boards for equality """
        for i in range(BOARD_SIZE * BOARD_SIZE):
            if self.pieces[i] == None:
                if other.pieces[i] == None:
                    continue
                return False
            if self.pieces[i] != other.pieces[i]:
                return False
        return True

    def __repr__(self):
        # TODO
        return ''


def create_board(pieces):
    """ Creates a board from a matrix of pieces """
    b = Board()
    for vidx in range(BOARD_SIZE):
        if len(pieces[vidx]) == 0:
            continue
        for hidx in range(BOARD_SIZE):
            elem = pieces[vidx][hidx]
            b[Position(hidx + 1, chr(vidx + ord('A')))] = elem
    return b


def new_board():
    """ Creates a new board with the starting pieces """
    board = Board()
    for idx, troop in enumerate(STARTING_BOARD[0]):
        board[Position(idx + 1, 'A')] = Piece(troop, Color.White)
        board[Position(idx + 1, 'I')] = Piece(troop, Color.Black)
    for idx, troop in enumerate(STARTING_BOARD[1]):
        board[Position(idx + 1, 'B')] = Piece(troop, Color.White)
        board[Position(idx + 1, 'H')] = Piece(troop, Color.Black)
    return board
