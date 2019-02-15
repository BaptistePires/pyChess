"""
    Queen piece class
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


class Queen(Piece):
    """
    Class description
    ---------------------------------------------------------------------------
    Attributes : See Piece class.
    """

    def __init__(self, x, y, code, player):
        """
        Constructor
        -----------------------------------------------------------------------
        Arguments : See Piece class.
        -----------------------------------------------------------------------
        Return : None.
        """
        super(Queen, self).__init__(x, y, code, player)

    def is_move_available(self, x, y, current_pl_pos, other_pl_pos, for_check):
        """
        See Piece class.
        -----------------------------------------------------------------------
        Arguments : See Piece class.
        -----------------------------------------------------------------------
        Return : See Piece class.
        """
        # Calling super class to format values
        current_pl_pos, other_pl_pos = super(Queen, self).is_move_available(x, y, current_pl_pos, other_pl_pos,
                                                                            for_check)

        # Check if the move is available
        if self.check_lateral_move(x, y, current_pl_pos, other_pl_pos) or self.check_diag_move(x, y, current_pl_pos,
                                                                                               other_pl_pos):
            return True
        else:
            return False

    def check_lateral_move(self, x, y, current_pl_pos, other_pl_pos):
        """
        Method to check if the Queen can move like the the rook.
        -----------------------------------------------------------------------
        Arguments : See is_move_available Piece method's.
        -----------------------------------------------------------------------
        Return : See is_move_available Piece method's.
        """
        # Getting the delats
        delta_x = self.getX() - x
        delta_y = self.getY() - y

        # If both deltas are not equals to deltas it means the
        # Queen is not going vertically or horizontally
        if delta_x != 0 and delta_y != 0:
            return False

        step = 1
        # Setting the the step and the max_for_loop value depending
        # of the direction of the piece
        if delta_x != 0 and delta_y == 0:
            if delta_x < 0:
                step = - 1
                max_for_loop = delta_x - 1
            else:
                max_for_loop = delta_x + 1

            # Checking if there is any pieces on the path of the Queen.
            for i in range(0, max_for_loop, step):
                next_pos = (self.getX() - i, self.getY())
                if next_pos in current_pl_pos or next_pos in other_pl_pos:
                    return False

        elif delta_y != 0 and delta_x == 0:
            if delta_y < 0:
                step = - 1
                max_for_loop = delta_y - 1
            else:
                max_for_loop = delta_y + 1

            # Checking if there is any pieces on the path of the Queen.
            for i in range(0, max_for_loop, step):
                next_pos = (self.getX(), self.getY() - i)
                if next_pos in current_pl_pos or next_pos in other_pl_pos:
                    return False

        return True

    def check_diag_move(self, x, y, current_pl_pos, other_pl_pos):
        """
        This method is used to check if the path that the Piece is taking is free or
        if another piece blocks it. Method took from Bishop.py

        :param x: Target x of the move
        :param y: Target y of the move
        :param other_pc_pos: List of positions of the pieces (current player pieces pos, other player pieces pos)
        :return: True if the path is free, else False
        """
        # Getting the deltas
        delta_x = self.getX() - x
        delta_y = self.getY() - y

        # Square that the Queen will go through
        squares = []

        if abs(delta_x) != abs(delta_y):
            return False
        else:
            # Setting squares value depending on which direction is going the Queen is going
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

        # for each square we check if there is any piece on it
        for sq in squares:
            if sq in other_pl_pos or sq in current_pl_pos:
                return False

        return True


if __name__ == '__main__':
    pass
