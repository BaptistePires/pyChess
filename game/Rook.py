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

    def is_move_avaible2(self, x, y, current_pl_pos, other_pl_pos):

        # TODO : bug piece peut se deplacecr n'immort ou
        returned = False
        # Remove the current piece from the player's pieces
        if (x, y) in other_pl_pos:
            other_pl_pos.remove((x, y))

        if self.getPos() in current_pl_pos:
            current_pl_pos.remove(self.getPos())

        # If the piece move and not stay at the same square
        if self.getX() == x and self.getY() == y:
            return False


        else:
            # Getting x, y delta's

            delta_x = self.getX() - x
            delta_y = self.getY() - y

            # If both deltas are higher than 1 than mean that the piece is not going
            # Verticaly or horizontaly
            if abs(delta_x) > 1 and abs(delta_y) > 1:
                return False

            can_move = False

            if abs(delta_x) != 0 and abs(delta_y) == 0:
                can_move = True
            elif abs(delta_y) != 0 and abs(delta_x) == 0:
                can_move = True

            if can_move:
                returned = True

                right = None
                up = None

                # Getting the direction
                if delta_x < 0:
                    right = True
                elif delta_x > 0:
                    right = False

                if delta_y < 0:
                    up = False
                elif delta_y > 0:
                    up = True

                max_range = 0
                step = 0
                # For each drirection we set up 2 vars :
                # - max_range : The range for the for loop after the test
                # - step : The step of the loop, because if max_range is lower than 1
                # then the loop need to decrement instead of increment
                if right:
                    # Going Right
                    max_range = delta_x - 1
                    step = - 1

                elif not right and right is not None:
                    # Going left
                    max_range = delta_x + 1
                    step = 1


                elif up:
                    # Going up
                    max_range = delta_y + 1
                    step = 1

                elif not up and up is not None:
                    max_range = delta_y - 1
                    step = - 1

                # Then we go for the number of square that the piece moved
                for i in range(0, max_range, step):
                    # We check what was the direction
                    if abs(delta_x) >= 1:
                        # If on the square that is on the path of the piece there already is
                        # an enemy or another piece of the current player then the piece can't move
                        if (self.getX() - i, self.getY()) in other_pl_pos:
                            returned = False
                        elif (self.getX() - i, self.getY()) in current_pl_pos:
                            returned = False
                    elif abs(delta_y) >= 1:
                        if (self.getX(), self.getY() - i) in other_pl_pos:
                            returned = False
                        elif (self.getX(), self.getY() - i) in current_pl_pos:
                            print((self.getX(), self.getY() - i))
                            returned = False

        print("ROOK : ", returned)
        return returned

    def check_jump(self, x, y, piece_pos):
        pass


if __name__ == '__main__':
    pass
