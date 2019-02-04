"""
    Class for #decrisption de la class
"""

# Module informations
__project__ = u''
__author__ = u'Pires Baptiste (baptiste.pires37@gmail.com)'
__date__ = u''
__version__ = u'1.0.0'

# Importations
import pygame

# Specific definitions


# Classes / Functions declaration


class HomeCanvas(pygame.Surface):
    """
    Class description
    ---------------------------------------------------------------------------
    Attributes :

    """

    def __init__(self, master, width, height, gui):
        """
        Constructor
        -----------------------------------------------------------------------
        Arguments :
        -----------------------------------------------------------------------
        Return : None.

        """
        super(HomeCanvas, self).__init__(size=(width, height))
        self.__width = width
        self.__height = height
        self.__gui = gui
        self.__master = master


    def draws(self):
        """
        Method used to draw all images needed
        -----------------------------------------------------------------------
        Arguments :

        -----------------------------------------------------------------------
        Return :
            None
        """
        # self.fill((255, 255, 255))
        self.draw_bg()

    def set_up(self):
        """
        Setting up the images and everything else
        :return:
        """

        self.set_up_bc_img()

    def set_up_bc_img(self):
        """
        Method used to load background image
        :return:
        """
        img = pygame.image.load("res/img/echiquier.png")
        self.__bg_img = pygame.transform.scale(img, (self.__gui.getWidth(), self.__gui.getHeight()))


    def draw_bg(self):
        self.fill((255,255,255))

if __name__ == '__main__':
    pass
