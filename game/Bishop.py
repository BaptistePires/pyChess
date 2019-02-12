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
from display.FlashMessage import FlashMessage
import display
# Specific definitions


# Classes / Functions declaration


class Bishop(Piece):
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
        super(Bishop, self).__init__(x, y, code, player)


    def is_move_avaible(self, x, y, current_pl_pos, other_pl_pos, for_check):
        current_pl_pos, other_pl_pos = super(Bishop, self).is_move_avaible(x, y, current_pl_pos, other_pl_pos, for_check)
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
            elif  delta_x > 0 and delta_y < 0:
                for i in range(0, delta_x + 1):
                    squares.append((self.getX() - i, self.getY() + i))
            elif delta_x > 0 and delta_y > 0:
                for i in range(0, delta_x + 1):
                    squares.append((self.getX() - i, self.getY() - i))


        for sq in squares:
            if sq in other_pl_pos or sq in current_pl_pos:
                return False

        return True

    def check_jump(self, x, y, other_pc_pos):
        """
        This method is used to check if the path that the Piece is taking is free or
        if another piece blocks it.

        :param x: Target x of the move
        :param y: Target y of the move
        :param other_pc_pos: List of positions of the pieces : (current player pieces pos, other player pieces pos)
        :return: True if the path is free, else False
        """

        # First, we remove the self pos of the piece
        if self.getPos() in other_pc_pos[0]:
            other_pc_pos[0].remove(self.getPos())

        # This will be used for the 'for' loop, because if we have a negative
        # end number, the loop wont loop, then it is used to loop even if so
        if self.getX() - x < 0:
            step_x = -1
        else:
            step_x = 1

        # Variables used to loop after we get the direction of the piece
        # loop_end : Number of loop needed to reach the target square
        # new_pos_format : Used to format operations
        loop_end = 0
        new_pos_format = ()

        # Check the direction the piece is going
        if self.getX() > x: # LEFT
            if self.getY() > y: # UP
                loop_end = self.getX() - x + 1
                new_pos_format = ('-','-')
            elif self.getY() < y: # DOWN
                loop_end = self.getX() - x + 1
                new_pos_format = ('-', '+')
        elif self.getX() < x: # RIGHT
            if self.getY() > y: # UP
                loop_end = self.getX() - x - 1
                new_pos_format = ('-', '+')
            elif self.getY() < y: # DOWN
                loop_end = self.getX() - x - 1
                new_pos_format = ('-', '-')

        # Loop the amount of square the piece need to move
        for i in range(0, loop_end, step_x):
            # Format the next pos, it means it calculate the next square the piece will go on
            if new_pos_format == ('-', '-'):
                next_pos = (self.getX() - i, self.getY() - i)
            else:
                next_pos = (self.getX() - i, self.getY() + i)

            # Check if we cross any piece of the current piece owner
            if next_pos in other_pc_pos[0] and self.getX() != x and self.getY() != y:
                return False

            # Check if we cross any piece of the player that is not currently playing.
            elif next_pos in other_pc_pos[1] and next_pos[0] != x and next_pos[1] != y:
                return False

        # If all these steps went well, then we return True
        return True

    def is_move_avaible2(self, x, y, current_pl_pos, other_pl_pos, for_check):
        super(Bishop, self).is_move_avaible(x, y, current_pl_pos, other_pl_pos, for_check=for_check)

        delta_x = abs(self.getX() - x)
        delta_y = abs(self.getY() - y)

        if delta_x == delta_y:
            if self.check_jump(x, y, (current_pl_pos, other_pl_pos)):
                return True
            else:
                return False
        else:
            return False


if __name__ == '__main__':
    pass
