"""
    GUI class
"""

# Module informations
__project__ = u''
__author__ = u'Pires Baptiste (baptiste.pires37@gmail.com)'
__date__ = u'28/01/19'
__version__ = u'1.0.0'

# Importations
from display.GameCanvas import GameCanvas
from display.HomeCanvas import HomeCanvas
import pygame
from BasicObjects.MyBaseProcess import MyBaseProcess
import time


# Specific definitions


# Classes / Functions declaration


class GUI(MyBaseProcess):
    """
    This class will be the GUI of the app.
    ---------------------------------------------------------------------------
    Attributes :
        - __window : window where the canvas will be displayed.
        - __main : main object.
        - __frame : canvas object currently displayed.
        - __icon : icon of the window.

    """

    def __init__(self, cfg, main):
        """
        Constructor
        -----------------------------------------------------------------------
        Arguments :
            - cfg : See MyBaseProcess class.
            - main : Main object
        -----------------------------------------------------------------------
        Return : None.
        """
        super(GUI, self).__init__(cfg)
        self.__window = None
        self.__main = main
        self.__canvas = None
        self.__icon = None

    def before_processing(self):
        """
        Method used to set up the GUI at the start of the app.
        -----------------------------------------------------------------------
        Arguments : None.
        -----------------------------------------------------------------------
        Return : None.
        """
        # Init pygame
        pygame.init()

        # Init the window
        self.__window = pygame.display.set_mode((self._ownConfig["def_w"], self._ownConfig["def_h"]))
        self.__icon = pygame.image.load("res/img/king-b.png")
        pygame.display.set_icon(self.__icon)

        # Init the home canvas.
        self.__canvas = HomeCanvas(self, self._ownConfig["def_w"], self._ownConfig["def_h"], gui=self, cfg=self._ownConfig["canvas"]["home"])
        self.__canvas.set_up()

        # 'Launching' the process
        self._isRunning = True



    def run(self):
        """
        Main loop of the GUI.
        -----------------------------------------------------------------------
        Arguments : None.
        -----------------------------------------------------------------------
        Return : None.
        """
        # Setting up everything
        self.before_processing()

        while self._isRunning:
            # Draw everything on the GUI
            self.__canvas.draws()
            self.__window.blit(self.__canvas, (0, 0))
            pygame.display.flip()

            # Handling events
            super(GUI, self).handle_self_events()
            self.__main.handle_events(pygame.event.get())


            time.sleep(0.001)

    ### GETTERS / SETTERS ###

    def getWidth(self):
        return self._ownConfig["def_w"]

    def getHeight(self):
        return self._ownConfig["def_h"]

    def set_game_canvas(self):
        self.__canvas = GameCanvas(self, self._ownConfig["def_w"], self._ownConfig["def_h"], gui=self, cfg=self._ownConfig["canvas"]["game"])
        self.__canvas.set_up()

    def getGrid(self):
        return self.__main.getGrid()

    def getPieces(self):
        return self.__main.getPieces()

    def set_stop_event(self):
        self._stopEvent.set()

    def getWindow(self):
        return self.__window

    def gerFrame(self):
        return self.__canvas

    def getButtons(self):
        return self.__canvas.getButtons()

    def set_state(self, state):
        self.__main.set_state(state)

    def get_flash_msgs(self):
        return self.__main.get_flash_msgs()

if __name__ == '__main__':
    pass
