"""
    This class is a class used to have the same base for
    all of the canvas.
"""

# Module informations
__project__ = u''
__author__ = u'Pires Baptiste (baptiste.pires37@gmail.com)'
__date__ = u''
__version__ = u'1.0.0'


# Importations
import pygame
from datetime import datetime

# Specific definitions


# Classes / Functions declaration


class BaseCanvas(pygame.Surface):
    """
    This class inherit pygame.Surface to be displayed on the pygame window.
    ---------------------------------------------------------------------------
    Attributes :
        - _ownConfig : Config of the canvas.
        - _width : Width of the canvas.
        - _height : Height of the canvas.
        - _gui : GUI object that will display the canvas.
        - _master : The window that the current canvas will be displayed on.
        - _bc_img : Background image of the canvas.
    """

    def __init__(self, width, height, gui, master, cfg):
        """
        Constructor
        -----------------------------------------------------------------------
        Arguments : See attributes above.
        -----------------------------------------------------------------------
        Return : None.
        
        """
        super(BaseCanvas, self).__init__(size=(width, height))
        self._ownConfig = cfg
        self._width = width
        self._height = height
        self._gui = gui
        self._master = master
        self._bg_img = None

    def draw_flash_messages(self):
        """
        This method is used to display Flash messages to users.
        -----------------------------------------------------------------------
        Arguments : None.
        -----------------------------------------------------------------------
        Return : None.
        """
        # All messages get in the current state through GUI and main classes
        msgs = self._gui.get_flash_msgs()

        for i, msg in enumerate(msgs):
            # print(msg.get_msg())
            # If It's the first time that the msg is displayed we init it
            if msg.get_first_display() == 0:
                msg.set_first_display(datetime.now())
                msg.set_up()
                x = (self._width - msg.getText().get_width()) / 2
                msg.setX(x)

            # Setting Y pos of the msg
            if i == 0:
                y = msg.getText().get_height() + (20 * i) + msgs[i].getText().get_height()
            else:
                y = msg.getText().get_height() + (40 * i) + msgs[i - 1].getText().get_height()

            msg.setY(y)

            # Time delta between 1st time displayed and now
            time_delta = datetime.now() - msg.get_first_display()

            if time_delta.total_seconds() <= msg.getDuration():
                # Borders and background
                pygame.draw.rect(self, msg.get_color_by_code(), pygame.Rect(msg.getX() - 3, msg.getY() - 3, msg.getText().get_width() + 6, msg.getText().get_height() + 6))
                pygame.draw.rect(self, (255, 255, 255), pygame.Rect(msg.getX(), msg.getY(), msg.getText().get_width(), msg.getText().get_height()))

                # The text
                self.blit(msg.getText(),
                          (msg.getX(), msg.getY()))
            else:
                # If the msg has been displayed the right amount of times
                self._gui.get_flash_msgs().pop(i)

    def draws(self):
        """
        Method used to draw everything on the canvas.
        -----------------------------------------------------------------------
        Arguments : None.
        -----------------------------------------------------------------------
        Return : None.
        """
        self.draw_flash_messages()

    def set_up(self):
        pass

    def set_up_bc_img(self):
        pass


if __name__ == '__main__':
    pass
    