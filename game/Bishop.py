"""
    Bishop Piece class
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


class Bishop(Piece):
    """
    Bishop piece class
    ---------------------------------------------------------------------------
    Attributes : See Piece Class.
    """

    def __init__(self, x, y, code, player):
        """
        Constructor
        -----------------------------------------------------------------------
        Arguments : See Piece Class.
        -----------------------------------------------------------------------
        Return : None.
        """
        super(Bishop, self).__init__(x, y, code, player)

    def is_move_available(self, x, y, current_pl_pos, other_pl_pos, for_check):
        """
        See Piece class.
        -----------------------------------------------------------------------
        Arguments : See Piece Class.
        -----------------------------------------------------------------------
        Return : See Piece Class.
        """
        # Calling super method to format the values
        current_pl_pos, other_pl_pos = super(Bishop, self).is_move_available(x, y, current_pl_pos, other_pl_pos,
                                                                             for_check)

        # Getting the delta of the move
        delta_x = self.getX() - x
        delta_y = self.getY() - y

        # List to store squares that the Pieces will go through
        squares = []

        # If the Bishop is not going diagonally
        if abs(delta_x) != abs(delta_y):
            return False
        else:
            # Setting up square list depending on which direction is going the bishop is going
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

        # For each square we chech if there is there is piece on it
        # If there is one, then we return False
        for sq in squares:
            if sq in other_pl_pos or sq in current_pl_pos:
                return False

        return True


if __name__ == '__main__':
    pass
