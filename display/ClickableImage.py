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
from BasicObjects.BaseWidget import BaseWidget
# Specific definitions


# Classes / Functions declaration


class ClickableImage(BaseWidget):
    """
    Class to display ClickableImage
    ---------------------------------------------------------------------------
    Attributes :
    
    """

    def __init__(self, x, y, width, height, img_path, action):
        """
        Constructor
        -----------------------------------------------------------------------
        Arguments :
        -----------------------------------------------------------------------
        Return : None.
        """
        super(ClickableImage, self).__init__(x=x, y=y, width=width, height=height, action=action)
        self.__img_path = img_path
        self.__img = None

    def set_up_img(self):
        """
        Method to set up the image
        -----------------------------------------------------------------------
        Arguments : See attributes above.
        -----------------------------------------------------------------------
        Return : None.
        """
        # Load and resize the image
        self.__img = pygame.image.load(self.__img_path)
        self.__img = pygame.transform.scale(self.__img, (self._width, self._height))


    ### GETTERS / SETTERS ###

    def get_img(self):
        return self.__img


if __name__ == '__main__':
    pass
    