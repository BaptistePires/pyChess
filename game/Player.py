"""
    Player class
"""

# Module informations
from game.Piece import Piece

__project__ = u''
__author__ = u'Pires Baptiste (baptiste.pires37@gmail.com)'
__date__ = u''
__version__ = u'1.0.0'

# Importations
from BasicObjects.BaseObject import BaseObject


# Specific definitions


# Classes / Functions declaration


class Player(BaseObject):
    """
    This is the player class.
    ---------------------------------------------------------------------------
    Attributes :
        - __game_state : GameState object.
        - __pieces : Pieces of the pieces.
        - __number : Number of the player.
        - __playing : Flag to know if the player is currently playing.
        - __isCheck : Flag to know if the player is under check.
    """

    def __init__(self, cfg, game, number):
        """
        Constructor
        -----------------------------------------------------------------------
        Arguments : See attributes above.
        -----------------------------------------------------------------------
        Return : None.
        """
        super(Player, self).__init__(config=cfg)
        self.__game_state = game
        self.__pieces = None
        self.__number = number
        self.__playing = False
        self.__isCheck = False

    def kill_piece(self, i):
        self.__pieces.pop(i)

    ### GETTERS / SETTERS ###

    def set_check(self, isCheck):
        self.__isCheck = isCheck

    def is_playing(self):
        return self.__playing

    def set_playing(self, p):
        self.__playing = p

    def getPieces(self):
        return self.__pieces

    def setPieces(self, p):
        self.__pieces = p

    def getNumber(self):
        return self.__number

    def get_king_pos(self):
        for p in self.getPieces():
            if p.getCode() == Piece.KING_CODE:
                return p.getPos()

    def is_check(self):
        return self.__isCheck

    def get_game(self):
        return self.__game_state

    def get_pieces_pos(self):
        returned_list = []

        for p in self.__pieces:
            returned_list.append(p.getPos())

        return returned_list

    def get_theme(self):
        return self.__game_state.get_theme()

    def get_piece_color_choice(self, nb):
        return self.__game_state.get_piece_color_choice(nb)

if __name__ == '__main__':
    pass
