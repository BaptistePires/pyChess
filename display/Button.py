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
# Specific definitions


# Classes / Functions declaration


class Button(object):
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

    def __init__(self, x, y, w, h, color, text, master, action, hover_color=(154,154,154)):
        """
        Constructor
        -----------------------------------------------------------------------
        Arguments : See attributes above.
        -----------------------------------------------------------------------
        Return : None.
        
        """
        self.__x = x
        self.__y = y
        self.__width = w
        self.__height = h
        self.__original_color = color
        self.__color = self.__original_color
        self.__hover_color = hover_color
        self.__text = text
        self.__master = master
        self.__action = action

    def action(self):
        """
        Action that the button has to perform when he's clicked.
        -----------------------------------------------------------------------
        Arguments : None.
        -----------------------------------------------------------------------
        Return : None.
        """
        if self.__action is not None:
            self.__action()

    def set_up(self):
        """
        Mehtod used to set u the buttons
        -----------------------------------------------------------------------
        Arguments : None.
        -----------------------------------------------------------------------
        Return : None.
        """
        # Default font for the button
        font = "res/font/good_time.ttf"

        # Setting up the text of it
        self.__text = TextToDisp(font=font,
                                  size=int(self.getWidth() / 10),
                                  text=self.__text,
                                  x=0, y=0, color=(255, 255, 255))

        self.__text.set_up()

        # Setting up x and y position of the text
        origin = self.getX()
        x = origin + (self.getWidth() - self.__text.getText().get_width()) / 2
        y_origin = self.getY()
        y = y_origin + (self.getHeight() - self.__text.getText().get_height()) / 2
        self.__text.setX(x)
        self.__text.setY(y)

    def hover(self, mx, my):
        if self.__x < mx < self.__x + self.__width and self.__y < my < self.__y + self.__height:
            self.__color = self.__hover_color
        else:
            self.__color = self.__original_color

# GETTERS / SETTERS

    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y

    def getRect(self):
        return pygame.Rect(self.__x, self.__y, self.__width, self.__height)

    def getColor(self):
        return self.__color

    def getText(self):
        return self.__text

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getWidth(self):
        return self.__width

    def getHeight(self):
        return self.__height


if __name__ == '__main__':
    pass
