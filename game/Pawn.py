"""
    Pawn piece class
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


class Pawn(Piece):
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
        super(Pawn, self).__init__(x, y, code, player)
        self.__isFirstMove = True

    def is_move_available(self, x, y, current_pl_pos, other_pl_pos, for_check):
        """
        See Piece class.
        -----------------------------------------------------------------------
        Arguments : See Piece Class.
        -----------------------------------------------------------------------
        Return : See Piece Class.
        """
        # Call super method to get the rights arrays
        current_pl_pos, other_pl_pos = super(Pawn, self).is_move_available(x, y, current_pl_pos, other_pl_pos,
                                                                           for_check=for_check)

        # Getting the x detla
        delta_x = self.getX() - x

        # Flag to check if the move is available
        can_move = False

        # There, we check where the piece is going
        if self._player.getNumber() == 1:
            # If it's first move
            if self.__isFirstMove:
                if self._y + 2 == y and delta_x == 0 or self._y + 1 == y and delta_x == 0:
                    can_move = True
            else:
                if self._y + 1 == y and delta_x == 0:
                    can_move = True
        else:
            if self.__isFirstMove:
                if self._y - 2 == y and delta_x == 0 or self._y - 1 == y and delta_x == 0:
                    can_move = True
            else:
                if self._y - 1 == y and delta_x == 0:
                    can_move = True
        if can_move:

            # Format value to loop the right way.
            # delta_y = The delta of the origin pos and the next one
            delta_y = self.getY() - y

            # The step of the for loop
            step = 1

            # This condition is needed to format the value for the loop
            if delta_y < 0:
                # If the pawn is going "down" on the grid
                step = - 1
                max_for_loop = delta_y - 1
            else:
                max_for_loop = delta_y + 1

            for i in range(0, max_for_loop, step):
                # Get the next square taht the pawn will go trough and check if there is any other piece on it
                next_pos = (self.getX(), self.getY() - i)
                if next_pos in current_pl_pos or next_pos in other_pl_pos:
                    return False

            # If it's first first move of the pawn then we set it to false
            if self.__isFirstMove:
                self.__isFirstMove = False

            self.move_cancel_check(1, 1)
            return True
        else:
            return False


if __name__ == '__main__':
    pass
