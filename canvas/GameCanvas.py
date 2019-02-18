"""
    GameCanvas class
"""

# Module informations
__project__ = u''
__author__ = u'Pires Baptiste (baptiste.pires37@gmail.com)'
__date__ = u''
__version__ = u'1.0.0'

# Importations
from BasicObjects.BaseCanvas import BaseCanvas
import pygame
from os import sep

# Specific definitions


# Classes / Functions declaration


class GameCanvas(BaseCanvas):
    """
    Class description
    ---------------------------------------------------------------------------
    Attributes :
        - __square_size : Size of a square in pixel. Need to be removed in
                            a next release.
    """

    def __init__(self, master, width, height, gui,cfg):
        """
        Constructor
        -----------------------------------------------------------------------
        Arguments : See attributes above.
        -----------------------------------------------------------------------
        Return : None.
        """
        super(GameCanvas, self).__init__(width=width, height=height, gui=gui, master=master, cfg=cfg)
        self._width += self._ownConfig["offsets"]["width"]
        self._height += self._ownConfig["offsets"]["height"]
        self.__square_size = 62.5
        self.__labels = []


    def draws(self):
        """
        Method used to draw all images needed
        -----------------------------------------------------------------------
        Arguments : None.
        -----------------------------------------------------------------------
        Return : None.
        """
        self.draw_grid()
        self.draw_entities()
        self.draw_flash_messages()

    def set_up(self):
        """
        Setting up the images and everything else
        :return:
        """
        self.set_up_entites_img()
        self.set_up_bc_img()

    def set_up_bc_img(self):
        """
        Method used to load background image
        :return:
        """
        img = pygame.image.load("res" + sep + "img" + sep + "theme_" + str(self._gui.get_theme()) + sep + "chess_plate.png")
        self._bg_img = pygame.transform.scale(img, (self._gui.getWidth(), self._gui.getHeight()))

    def set_up_entites_img(self):
        """
        Method used to load entities img
        :return:
        """
        for p_player in self._gui.getPieces():
            for  piece in p_player:
                piece.set_img()

    def draw_entities(self):
        """
        Method used to draw all entities
        :return:
        """
        # We get all the pieces of the players
        players_pieces = self._gui.getPieces()

        # For each player
        for p_player in players_pieces:
            # For each player's piece
            for i, piece in enumerate(p_player):
                # If the piece is not selected
                if not piece.is_selected():
                    # Setting up the x, y pos of the piece
                    y = piece.getY() * self.__square_size + int(15 / 2)
                    x = int(piece.getX() * self.__square_size) + int(15 / 2)
                    self.blit(piece.getImg(), (x, y))
                else:
                    # If the piece is selected, then we need to make it follow the mouse
                    self.blit(piece.getImg(), (
                    int(pygame.mouse.get_pos()[0] - (62.5 / 2)), int(pygame.mouse.get_pos()[1] - (62.5 / 2))))

    def draw_grid(self):
        """
        Method used to draw the grid
        """
        self.blit(self._bg_img, (0, 0))


    def disp_case_i(self, grid):
        """
        Method used to draw squares indexes on the screen used for debug because it use a lot of ressources
        :param grid:
        :return:
        """
        for i in grid:
            for j in range(8):
                myfont = pygame.font.SysFont("monospace", 15)
                # render text
                label = myfont.render("[" + str(j) + ";" + str(i) + ']', 1, (0, 0, 0))
                self.blit(label, ((j * self.__square_size) + 7, (i * self.__square_size) + 7))


if __name__ == '__main__':
    pass
