"""
    Class for #decrisption de la class
"""

# Module informations
__project__ = u''
__author__ = u'Pires Baptiste (baptiste.pires37@gmail.com)'
__date__ = u''
__version__ = u'1.0.0'

# Importations
from game.Piece import Piece
from game.Rook import Rook
from game.Bishop import Bishop


# Specific definitions


# Classes / Functions declaration


class Queen(Piece):
    """
    Class description
    ---------------------------------------------------------------------------
    Attributes :

    """

    def __init__(self, x, y, code, player):
        """
        Constructor
        -----------------------------------------------------------------------
        Arguments :
        -----------------------------------------------------------------------
        Return : None.

        """
        super(Queen, self).__init__(x, y, code, player)

    def is_move_avaible(self, x, y, current_pl_pos, other_pl_pos, for_check):
        """
        Method description
        -----------------------------------------------------------------------
        Arguments :

        -----------------------------------------------------------------------
        Return :
            None
            :param for_check:
        """
        current_pl_pos, other_pl_pos = super(Queen, self).is_move_avaible(x, y, current_pl_pos, other_pl_pos,
                                                                           for_check)
        if self.check_lateral_move(x, y, current_pl_pos, other_pl_pos) or self.check_diag_move(x,y, current_pl_pos, other_pl_pos):
            return True
        else:
            return False

    def check_lateral_move(self, x, y, current_pl_pos, other_pl_pos):
        delta_x = self.getX() - x
        delta_y = self.getY() - y
        if delta_x != 0 and delta_y != 0:
            return False

        step = 1
        if delta_x != 0 and delta_y == 0:
            if delta_x < 0:
                step = - 1
                max = delta_x - 1

            else:
                max = delta_x + 1

            for i in range(0, max, step):
                next_pos = (self.getX() - i, self.getY())
                if next_pos in current_pl_pos or next_pos in other_pl_pos:
                    return False

        elif delta_y != 0 and delta_x == 0:
            if delta_y < 0:
                step = - 1
                max = delta_y - 1
            else:
                max = delta_y + 1

            for i in range(0, max, step):
                next_pos = (self.getX(), self.getY() - i)
                if next_pos in current_pl_pos or next_pos in other_pl_pos:
                    return False

        # print(next_pos)

        return True

    def check_diag_move(self, x, y, current_pl_pos, other_pl_pos):
        """
        This method is used to check if the path that the Piece is taking is free or
        if another piece blocks it. Method took from Bishop.py

        :param x: Target x of the move
        :param y: Target y of the move
        :param other_pc_pos: List of positions of the pieces : (current player pieces pos, other player pieces pos)
        :return: True if the path is free, else False
        """
        delta_x = self.getX() - x
        delta_y = self.getY() - y
        squares = []

        if abs(delta_x) != abs(delta_y):
            return False
        else:
            if delta_x < 0 and delta_y < 0:
                for i in range(0, delta_x - 1, -1):
                    squares.append((self.getX() - i, self.getY() - i))
            elif delta_x < 0 and delta_y > 0:
                for i in range(0, delta_x - 1, -1):
                    squares.append((self.getX() - i, self.getY() + i))
            elif delta_x > 0 and delta_y < 0:
                for i in range(0, delta_x + 1):
                    squares.append((self.getX() - i, self.getY() + i))
            elif delta_x > 0 and delta_y > 0:
                for i in range(0, delta_x + 1):
                    squares.append((self.getX() - i, self.getY() - i))

        for sq in squares:
            if sq in other_pl_pos or sq in current_pl_pos:
                return False

        return True


if __name__ == '__main__':
    pass
