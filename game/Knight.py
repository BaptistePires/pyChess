"""
    Knight piece class
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


class Knight(Piece):
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
        super(Knight, self).__init__(x, y, code, player)

    def is_move_available(self, x, y, current_pl_pos, other_pl_pos, for_check):
        """
        See Piece class.
        -----------------------------------------------------------------------
        Arguments : See Piece Class.
        -----------------------------------------------------------------------
        Return : See Piece Class.
        """
        # Calling super method to formate values
        current_pl_pos, other_pl_pos = super(Knight, self).is_move_available(x, y, current_pl_pos, other_pl_pos,
                                                                             for_check=for_check)

        # if there is a piece of the current player or if the current knight is on the square
        if (x, y) in current_pl_pos or (x, y) == self.getPos():
            return False

        returned = False

        # Check if the move is avaible, no need to check if
        # there is any piece on the the path of the knight
        # because he can jump over it
        if self._y + 2 == y and self._x + 1 == x:
            returned = True
        elif self._y + 2 == y and self._x - 1 == x:
            returned = True
        elif self._y - 2 == y and self._x - 1 == x:
            returned = True
        elif self._y - 2 == y and self._x + 1 == x:
            returned = True
        elif self._y - 1 == y and self._x - 2 == x:
            returned = True
        elif self._y + 1 == y and self._x - 2 == x:
            returned = True
        elif self._y - 1 == y and self._x + 2 == x:
            returned = True
        elif self._y + 1 == y and self._x + 2 == x:
            returned = True
        else:
            returned = False

        return returned


if __name__ == '__main__':
    pass
