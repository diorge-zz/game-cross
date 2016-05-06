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

    def test_position_parsing_incorrect(self):
        """ Tests position parsing for incorrect input """
        a, b, c = '', '0A', '4c'
        with self.assertRaises(ValueError) as ctx:
            cgame.Position.parse(a)
        with self.assertRaises(ValueError) as ctx:
            cgame.Position.parse(b)
        with self.assertRaises(ValueError) as ctx:
            cgame.Position.parse(c)

    def test_piece_repr(self):
        """ Tests the representation of the pieces """
        p1 = cgame.Piece(cgame.TroopType.Swordsman, cgame.Color.White)
        p2 = None
        p3 = cgame.Piece(cgame.TroopType.Horseman, cgame.Color.Black)
        assert 'WW' == cgame.piece_repr(p1)
        assert '00' == cgame.piece_repr(p2)
        assert 'HB' == cgame.piece_repr(p3)

    def test_initial_board_repr(self):
        """ Tests the board representation for the initial board """
        b = cgame.new_board()
        s = repr(b)
        empty_row = '-'.join(['00'] * 9)
        empty_rows = '/'.join([empty_row] * 5)
        white_rows = ('PW-WW-WW-HW-GW-HW-WW-WW-PW' + '/' +
                      'PW-PW-WW-AW-AW-AW-WW-PW-PW')
        black_rows = ('PB-PB-WB-AB-AB-AB-WB-PB-PB' + '/' +
                      'PB-WB-WB-HB-GB-HB-WB-WB-PB')
        expected = '/'.join([white_rows, empty_rows, black_rows])
        assert expected == s
