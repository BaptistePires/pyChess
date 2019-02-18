"""
    GUI class
"""

# Module informations
__project__ = u''
__author__ = u'Pires Baptiste (baptiste.pires37@gmail.com)'
__date__ = u'28/01/19'
__version__ = u'1.0.0'

# Importations
from canvas.GameCanvas import GameCanvas
from canvas.HomeCanvas import HomeCanvas
import pygame
from BasicObjects.MyBaseProcess import MyBaseProcess
import time
from importlib import import_module

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
        self.__current_state_name = ""

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
            self.set_up_canvas()
            self.__canvas.draws()
            self.__window.blit(self.__canvas, (0, 0))
            pygame.display.flip()

            # Handling events
            super(GUI, self).handle_self_events()
            self.__main.handle_events(pygame.event.get())


            time.sleep(0.001)


    def set_up_canvas(self):

        current_state = self.__main.get_current_state()

        if self.__current_state_name == current_state:
            return

        # Setting up the class name
        class_name = current_state.capitalize() + "Canvas"

        # There we check if the current state is not the same
        if type(self.__canvas).__name__ != class_name:
            # Creating dynamically the state class
            try:
                # Import library
                module = import_module("canvas." + class_name)

                if class_name:
                    state_class = getattr(module, class_name)
                    # Setting the current state got in parameters as the new state
                    self.__canvas = state_class(gui=self, cfg=self._ownConfig["canvas"][current_state.lower()], master=self.__window,width=self._ownConfig["def_w"], height=self._ownConfig["def_h"])
                    self.__canvas.set_up()
                    # self.__state.launch()
                    self.__current_state_name = current_state
                    # self.__gui.set_game_canvas()

            except Exception as exc:
                print(
                    "Can't import : {lib}".format(lib=class_name))
                print(
                    "Error message : {msg}".format(msg=exc.args))

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
