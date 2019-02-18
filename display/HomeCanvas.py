"""
    HomeCanvas class
"""

# Module informations
__project__ = u''
__author__ = u'Pires Baptiste (baptiste.pires37@gmail.com)'
__date__ = u''
__version__ = u'1.0.0'

# Importations
from BasicObjects.BaseCanvas import BaseCanvas
import pygame
from display.TextToDisp import TextToDisp
from display.Button import Button
# Specific definitions


# Classes / Functions declaration


class HomeCanvas(BaseCanvas):
    """
    Canvas for the home of the game
    ---------------------------------------------------------------------------
    Attributes :
        - width, height, gui, master, cgf : See BaseCanvas class from display package.
        - __bg_color : Background color of the canvas.
        - __title : Title displayed on it.
        - __buttons : Buttons of the canvas.
    """

    def __init__(self, master, width, height, gui, cfg):
        """
        Constructor
        -----------------------------------------------------------------------
        Arguments : See attributes above.
        -----------------------------------------------------------------------
        Return : None.

        """
        super(HomeCanvas, self).__init__(width=width, height=height, gui=gui, master=master, cfg=cfg)
        self.__bg_color = (255, 255, 255)
        self.__title = None
        self.__buttons = []

    def draws(self):
        """
        Method used to draw everything on it.
        -----------------------------------------------------------------------
        Arguments : None.
        -----------------------------------------------------------------------
        Return : None.
        """
        # self.fill((255, 255, 255))
        self.draw_bg()
        self.draw_title()
        self.draw_buttons()

    def set_up_title(self):
        """
        Method used set up the title of the canvas.
        -----------------------------------------------------------------------
        Arguments : None.
        -----------------------------------------------------------------------
        Return : None.
        """
        # Font of the text.
        font = "res/font/good_time.ttf"
        # Creating and setting up the text
        self.__title = TextToDisp(font=font,
                                  size=60,
                                  text="pyChess",
                                  x=100,
                                  y=100, color=(0,0,0))

        self.__title.set_up()

        # Setting its x, y pos
        x = (self._width - self.__title.getText().get_width()) / 2
        y = self.__title.getText().get_height() + 10

        self.__title.setX(x)
        self.__title.setY(y)

    def set_up_buttons(self):
        """
        Method used to set_up buttons of the canvas
        -----------------------------------------------------------------------
        Arguments : None.
        -----------------------------------------------------------------------
        Return : None.
        """
        # Buttons width and height
        b_w = 200
        b_h = 50

        # Creating and settign up first button : @TODO : In a future release it will be in the config file
        button = Button(x=0, y=0, w=b_w, h=b_h, color=(0,0,0), text="Settings", master=self, action=None)

        x = (self.get_width() - b_w) / 2
        y = self.get_height() - 110
        button.setX(x)
        button.setY(y)
        button.set_up()

        # Add it to the button list
        self.__buttons.append(button)

        # Creating and settign up second button
        button = Button(x=0, y=0, w=b_w, h=b_h, color=(0, 0, 0), text="Play !", master=self, action=self.set_game_state)

        x = (self.get_width() - b_w) / 2
        y = self.get_height() - 110 - b_h - 10
        button.setX(x)
        button.setY(y)
        button.set_up()

        self.__buttons.append(button)

    def set_game_state(self):
        self.set_state("game")
    def draw_buttons(self):
        """
        Method used to draw the button on the canvas.
        -----------------------------------------------------------------------
        Arguments : None.
        -----------------------------------------------------------------------
        Return : None.
        """
        for b in self.__buttons:
            pygame.draw.rect(self, b.getColor(), b.getRect())
            self.blit(b.getText().getText(), (b.getText().getX(), b.getText().getY()))

    def draw_title(self):
        """
        Method used to draw the title on the canvas.
        -----------------------------------------------------------------------
        Arguments : None.
        -----------------------------------------------------------------------
        Return : None.
        """
        self.blit(self.__title.getText(),
                    (self.__title.getX(), self.__title.getY()))


    def set_up(self):
        """
        Setting up the images and everything else
        :return:
        """
        self.set_up_title()
        self.set_up_buttons()

    def draw_bg(self):
        """
        Method used to draw the background
        -----------------------------------------------------------------------
        Arguments : None.
        -----------------------------------------------------------------------
        Return : None.
        """
        self.fill(self.__bg_color)

    ### GETTERS / SETTERS ###

    def getButtons(self):
        return self.__buttons

    def set_state(self, state):
        self._master.set_state(state)

if __name__ == '__main__':
    pass
