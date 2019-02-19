"""
    Class for #decrisption de la class
"""

# Module informations
__project__ = u''
__author__ = u'Pires Baptiste (baptiste.pires37@gmail.com)'
__date__ = u''
__version__ = u'1.0.0'


# Importations
from BasicObjects.BaseCanvas import BaseCanvas
from display.TextToDisp import TextToDisp
from time import strftime
import pygame
# Specific definitions


# Classes / Functions declaration


class LogCanvas(BaseCanvas):
    """
    This class is a logger that is used to display info to the user.
    ---------------------------------------------------------------------------
    """

    def __init__(self, master, width, height, gui, cfg, bg_color):
        """
        Constructor
        -----------------------------------------------------------------------
        Arguments : See super class.
            - bg_color : Background color of the logger
        -----------------------------------------------------------------------
        Return : None.
        """
        super(LogCanvas, self).__init__(width=width, height=height, gui=gui, master=master, cfg=cfg)
        self.__bg_color = bg_color
        self.__bg_borders = None
        self.__bg = None

    def set_up(self):
        self.set_up_bg()

    def draws(self):
        self.draw_bg()
        self.draw_strings()
        self.check_if_string_is_on_screen()

    def draw_border(self):
        pygame.draw.rect(self, (0,0,0),
                         pygame.Rect(0, 0, self.get_width(), self.get_height()))
    def draw_bg(self):
        pygame.draw.rect(self,  (0,0,0),
                         self.__bg_borders)

        pygame.draw.rect(self,  self.__bg_color,
                         self.__bg)

    def set_up_bg(self):
        self.__bg_borders = pygame.Rect(0, 0, self.get_width(), self.get_height())

        self.__bg = pygame.Rect( 2,2, self.get_width() - 4, self.get_height() - 4)
    def draw_strings(self):
        if len(self.get_strings()) > 0:
            for i, string in enumerate(reversed(self.get_strings())):
                if i == 0:
                    y = self.get_height() - 16
                else:
                    y = self.get_height() - (16 * (i + 1))

                string.setY(y)
                self.blit(string.getText(),
                          (string.getX(), string.getY()))

    def check_if_string_is_on_screen(self):
        for string in self.get_strings():
            if string.getY() < 0:
                self.get_strings().remove(string)

    def add_msg(self, msg_text):
        text = strftime("%H:%M:%S") + " : "
        text += msg_text
        # Font of the text.
        font = "res/font/terminal_font.ttf"

        # print(str(len(self.get_strings())))
        if len(self._strings) == 0 :
            y = self.get_height() - 16
        else:
            y = self._strings[-1].getY() - self._strings[-1].getText().get_height() - 1

        # y = 15 + (15 * len(self.get_strings()) - 1)
        # Creating and setting up the text
        new_str = TextToDisp(font=font,
                             size=12,
                             text=text,
                             x=10,
                             y=y, color=(0, 0,0 ))

        new_str.set_up()
        self._strings.append(new_str)

if __name__ == '__main__':
    pass
    