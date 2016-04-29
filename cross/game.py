from enum import Enum


class TroopType(Enum):
    Swordsman = 1
    Spearman = 2
    Archer = 3
    Horseman = 4
    General = 5


class Color(Enum):
    Black = 0
    White = 1


class Piece(object):
    """ Piece on the board """

    def __init__(self, trooptype, color):
        """ Instantiates a new piece"""
        self.trooptype = trooptype
        self.color = color
