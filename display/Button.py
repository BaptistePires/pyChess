"""
    Button class
"""

# Module informations
__project__ = u''
__author__ = u'Pires Baptiste (baptiste.pires37@gmail.com)'
__date__ = u''
__version__ = u'1.0.0'


# Importations
from display.TextToDisp import TextToDisp
import pygame
from BasicObjects.BaseWidget import BaseWidget
# Specific definitions


# Classes / Functions declaration


class Button(BaseWidget):
    """
    Class description
    ---------------------------------------------------------------------------
    Attributes :
        - __x : x position of the button.
        - __y : y position of the button.
        - __width : width of the button.
        - __height : height of the button.
        - __text : text of the button.
        . __color : Color of the button.
        - __master : BaseCanvas or child object
    
    """

    def __init__(self, x, y, width, height, color, text, master, action, hover_color=(154,154,154)):
        """
        Constructor
        -----------------------------------------------------------------------
        Arguments : See attributes above.
        -----------------------------------------------------------------------
        Return : None.
        
        """
        super(Button, self).__init__(x=x, y=y, width=width, height=height, action=action)
        self.__original_color = color
        self.__color = self.__original_color
        self.__hover_color = hover_color
        self.__text = text
        self.__master = master

    def set_up(self):
        """
        Mehtod used to set u the buttons
        -----------------------------------------------------------------------
        Arguments : None.
        -----------------------------------------------------------------------
        Return : None.
        """
        # Default font for the button
        font = "res/font/GOOD_DADDY.otf"

        # Setting up the text of it
        self.__text = TextToDisp(font=font,
                                  size=int(self.get_width() / 10),
                                  text=self.__text,
                                  x=0, y=0, color=(255, 255, 255))

        self.__text.set_up()

        # Setting up x and y position of the text
        origin = self.get_x()
        x = origin + (self.get_width() - self.__text.getText().get_width()) / 2
        y_origin = self.get_y()
        y = y_origin + (self.get_height() - self.__text.getText().get_height()) / 2
        self.__text.setX(x)
        self.__text.setY(y)

    def hover(self, mx, my):
        if self._x < mx < self._x + self._width and self._y < my < self._y + self._height:
            self.__color = self.__hover_color
        else:
            self.__color = self.__original_color

# GETTERS / SETTERS
    def getRect(self):
        return pygame.Rect(self._x, self._y, self._width, self._height)

    def getColor(self):
        return self.__color

    def getText(self):
        return self.__text



if __name__ == '__main__':
    pass
