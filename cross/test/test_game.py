from unittest import TestCase
import cross.game as cgame


class TestGame(TestCase):
    """ Test suite for the basic game logic """

    def test_piece_instantiation(self):
        p = cgame.Piece(cgame.TroopType.Spearman, cgame.Color.White)
        assert p.trooptype == cgame.TroopType.Spearman
        assert p.color == cgame.Color.White

    def test_position_index(self):
        """ Tests conversion of (H, V) coordinate to 0-based index """
        zero = cgame.Position(1, 'A')
        idx = cgame.Position(4, 'C')
        final = cgame.Position(9, 'I')
        assert 0 == zero.index
        assert 21 == idx.index
        assert 80 == final.index

    def test_starting_board(self):
        """ Tests the validity of the starting board """
        starting = cgame.new_board()
        sw, sp, a, h, g = cgame.TroopType.__iter__()
        b, w = cgame.Color.__iter__()
        p = cgame.Piece
        expected = cgame.create_board([
            [p(sp, w), p(sw, w), p(sw, w),
                p(h, w), p(g, w), p(h, w),
                p(sw, w), p(sw, w), p(sp, w)],
            [p(sp, w), p(sp, w), p(sw, w),
                p(a, w), p(a, w), p(a, w),
                p(sw, w), p(sp, w), p(sp, w)],
            [], [], [], [], [],
            [p(sp, b), p(sp, b), p(sw, b),
                p(a, b), p(a, b), p(a, b),
                p(sw, b), p(sp, b), p(sp, b)],
            [p(sp, b), p(sw, b), p(sw, b),
                p(h, b), p(g, b), p(h, b),
                p(sw, b), p(sw, b), p(sp, b)]
            ])
        assert expected == starting

    def test_position_parsing_correct(self):
        """ Tests position parsing with correct input """
        a, b, c = '1A', '5D', '9I'
        ra, rb, rc = map(cgame.Position.parse, [a, b, c])
        assert ra.index == 0
        assert rb.index == 31
        assert rc.index == 80
