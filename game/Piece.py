"""
    Class for #decrisption de la class
"""

# Module informations
__project__ = u''
__author__ = u'Pires Baptiste (baptiste.pires37@gmail.com)'
__date__ = u''
__version__ = u'1.0.0'

# Importations
from os import sep
import pygame
from display.FlashMessage import FlashMessage


# Specific definitions


# Classes / Functions declaration


class Piece(object):
    """
    Class description
    ---------------------------------------------------------------------------
    Attributes :
        - x : x Pos of the piece.
        - y : y pos if the piece.
        - code : Code of the piece.
        - player : Player object that is the 'owner' of the piece.
        - img : Img of the piece.
        - width : width of the piece.
        - selected : Flag used to know if the piece is selected.
    """

    # Const TODO: Check why it's not working when it outside the class
    KING_CODE = 0
    QUEEN_CODE = 1
    ROOK_CODE = 2
    BISHOP_CODE = 3
    KNIGHT_CODE = 4
    PAWN_CODE = 5

    # Player number for the colors
    NUMBER_1_COLOR = "w"
    NUMBER_2_COLOR = "b"

    def __init__(self, x, y, code, player):
        """
        Constructor
        -----------------------------------------------------------------------
        Arguments : See Piece Class.
        -----------------------------------------------------------------------
        Return : None.
        """
        self._x = x
        self._y = y
        self._code = code
        self._player = player
        self._img = None
        self._width = 62.5
        self._selected = False


    def __str__(self):
        """
        Method called when you print a piece.
        -----------------------------------------------------------------------
        Arguments : None.
        -----------------------------------------------------------------------
        Return : None.
        """
        returned_str = ""
        returned_str += self.code_to_str() + " " + str(self.getColor()) + "\n"
        returned_str += "pos : [" + str(self._x) + "," + str(self._y) + "] \n"
        returned_str += "player : " + str(self._player.getNumber()) + "\n"
        returned_str += "------------------------------"
        return returned_str

    def selected(self):
        if self._selected:
            self._selected = False
        else:
            self._selected = True

    ### GETTERS / SETTERS ###

    def set_img(self):
        """
        Method called to set the img to the piece.
        -----------------------------------------------------------------------
        Arguments : None.
        -----------------------------------------------------------------------
        Return : None.
        """
        # Method used to set_up the img of the piece
        path = "res" + sep + "img" + sep + "pieces" + sep + str(self.get_piece_color_choice())+ sep + self.code_to_str() + ".png"
        self._img = pygame.image.load(path)
        self._img = pygame.transform.scale(self._img, (int(62.5 - 15), int(62.5 - 15)))
        self._is_first_move = False

    def getColor(self):
        if self._player.getNumber() == 1:
            return self.NUMBER_1_COLOR
        else:
            return self.NUMBER_2_COLOR

    def is_selected(self):
        return self._selected

    def getWidth(self):
        return self._width

    def getCode(self):
        return self._code

    def getImg(self):
        return self._img

    def getX(self):
        return self._x

    def getPos(self):
        return self._x, self._y

    def getY(self):
        return self._y

    def check_jump(self, x, y, other_pc_pos):
        pass

    def set_x(self, x):
        self._x = x

    def set_y(self, y):
        self._y = y

    def is_move_available(self, x, y, current_pl_pos, other_pl_pos, for_check):

        if (x, y) in other_pl_pos:
            other_pl_pos.remove((x, y))
        if self.getPos() in current_pl_pos:
            current_pl_pos.remove(self.getPos())

        return current_pl_pos, other_pl_pos

    def move_cancel_check(self, x, y):
        pass

    def new_pos(self, x, y):
        self._x = x
        self._y = y

    def getPlayerNumber(self):
        return self._player.getNumber()

    def is_alive(self):
        return True

    def code_to_str(self):
        if self._code == 0:
            return "king"
        elif self._code == 1:
            return "queen"
        elif self._code == 2:
            return "rook"
        elif self._code == 3:
            return "bishop"
        elif self._code == 4:
            return "knight"
        else:
            return "pawn"

    def get_piece_color_choice(self):
        return self._player.get_piece_color_choice(self._player.getNumber())


if __name__ == '__main__':
    pass
