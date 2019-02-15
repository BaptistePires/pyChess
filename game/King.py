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


class King(Piece):
    """
    King piece class
    ---------------------------------------------------------------------------
    Attributes : See Piece Class.
        - __isFirstMove : Flag to know if the move is the first one
    """

    def __init__(self, x, y, code, player):
        """
        Constructor
        -----------------------------------------------------------------------
        Arguments : See Piece Class.
        -----------------------------------------------------------------------
        Return : None.
        """
        super(King, self).__init__(x, y, code, player)
        self.__isFirstMove = True

    def is_move_available(self, x, y, current_pl_pos, other_pl_pos, for_check):
        """
        See Piece class.
        -----------------------------------------------------------------------
        Arguments : See Piece Class.
        -----------------------------------------------------------------------
        Return : See Piece Class.
        """
        # Calling super method to format the values
        current_pl_pos, other_pl_pos = super(King, self).is_move_available(x, y, current_pl_pos, other_pl_pos,
                                                                           for_check=for_check)

        # Getting delta of the move
        delta_x = self.getX() - x
        delta_y = self.getY() - y

        # If the King move than more than 1 square
        if not -1 <= delta_x <= 1 or not -1 <= delta_y <= 1:
            return False

        next_pos = (0, 0)
        # Getting the next pos of the piece
        if delta_x != 0 and delta_y == 0:
            if delta_x < 0:
                next_pos = (self.getX() + 1, self.getY())
            else:
                next_pos = (self.getX() - 1, self.getY())
        elif delta_y != 0 and delta_x == 0:
            if delta_y < 0:
                next_pos = (self.getX(), self.getY() + 1)
            else:
                next_pos = (self.getX(), self.getY() - 1)
        else:
            if delta_x > 0 and delta_y > 0:
                next_pos = (self.getX() - 1, self.getY() - 1)
            elif delta_x > 0 and delta_y < 0:
                next_pos = (self.getX() - 1, self.getY() + 1)
            elif delta_x < 0 and delta_y > 0:
                next_pos = (self.getX() + 1, self.getY() - 1)
            elif delta_x < 0 and delta_y < 0:
                next_pos = (self.getX() + 1, self.getY() + 1)

        # If there is an ally in the next pos
        if next_pos in current_pl_pos:
            return False
        else:
            return False


if __name__ == '__main__':
    pass
