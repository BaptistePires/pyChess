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


# Specific definitions


# Classes / Functions declaration


class Rook(Piece):
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
        super(Rook, self).__init__(x, y, code, player)

    def is_move_avaible(self, x, y, current_pl_pos, other_pl_pos, for_check):
        current_pl_pos, other_pl_pos = super(Rook, self).is_move_avaible(x, y, current_pl_pos, other_pl_pos, for_check=for_check)
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

    def check_jump(self, x, y, piece_pos):
        pass


if __name__ == '__main__':
    pass
