"""
    Class for #decrisption de la class
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
    Class description
    ---------------------------------------------------------------------------
    Attributes :
    
    """

    def __init__(self, cfg, game, number):
        """
        Constructor
        -----------------------------------------------------------------------
        Arguments :
        -----------------------------------------------------------------------
        Return : None.
        
        """
        super(Player, self).__init__(config=cfg)
        self.__game = game
        self.__pieces = None
        self.__number = number
        self.__playing = False
        self.__check = False


    def check_check(self, current_pl_pos, other_pl_pos):

        king_pos = self.get_king_pos()
        player_pos, other_player = self.__game.getPlayersPos(self.getNumber())
        for other_p in other_pl_pos:
            if other_p.is_move_avaible(king_pos[0], king_pos[1], other_player, player_pos, True):
                print("check by piece at :", other_p.getPos())

    def is_playing(self):
        return self.__playing

    def set_playing(self, p):
        self.__playing = p
        if not p:
            return
            self.__game.check_check(self.getNumber())

    def getPieces(self):
        return self.__pieces

    def setPieces(self, p):
        self.__pieces = p

    def getNumber(self):
        return self.__number

    def kill_piece(self, i):
        # print("Player / Killed : \n", self.__pieces[i])
        self.__pieces.pop(i)

    def get_king_pos(self):
        for p in self.getPieces():
            if p.getCode() == Piece.KING_CODE:
                return p.getPos()


    def isCheck(self):
        return self.__check

if __name__ == '__main__':
    pass
    