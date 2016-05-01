from unittest import TestCase
import cross.game as cgame


class TestGame(TestCase):
    """ Test suite for the basic game logic """

    def test_piece_instantiation(self):
        p = cgame.Piece(cgame.TroopType.Spearman, cgame.Color.White)
        assert p.trooptype == cgame.TroopType.Spearman
        assert p.color == cgame.Color.White

    def test_starting_board(self):
        """ Tests the validity of the starting board """
        b = cgame.new_board()
        sp, sw, a, h, g = cgame.TroopType.__iter__()
        b, w = cgame.Color.__iter__()
        p = cgame.Piece
        expected = cgame.Board([
            [p(sp, w), p(sw, w), p(sw, w), p(h, w), p(g, w), p(h, w), p(sw, w), p(sw, w), p(sp, w)],
            [p(sp, w), p(sp, w), p(sw, w), p(a, w), p(a, w), p(a, w), p(sw, w), p(sp, w), p(sp, w)],
            [], [], [], [], [],
            [p(sp, b), p(sp, b), p(sw, b), p(a, b), p(a, b), p(a, b), p(sw, b), p(sp, b), p(sp, b)],
            [p(sp, b), p(sw, b), p(sw, b), p(h, b), p(g, b), p(h, b), p(sw, b), p(sw, b), p(sp, b)]])
        assert expected == b
