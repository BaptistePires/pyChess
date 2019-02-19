"""
    GUI class
"""

# Module informations
from display.FlashMessage import WARNING_CODE, FlashMessage, INFO_CODE

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
        self.__grid_choice = 1
        self.__player_1_pieces_color = "white"
        self.__player_2_pieces_color = "black"

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

        # Setting up the icon and the title
        pygame.display.set_icon(pygame.transform.scale(pygame.image.load("res/img/icon.png"), (32, 32)))
        pygame.display.set_caption('pyChess')

        # Init the home canvas
        self.__canvas = HomeCanvas(self, self._ownConfig["def_w"], self._ownConfig["def_h"], gui=self,
                                   cfg=self._ownConfig["canvas"]["home"])
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
                    self.__canvas = state_class(gui=self, cfg=self._ownConfig["canvas"][current_state.lower()],
                                                master=self.__window, width=self._ownConfig["def_w"],
                                                height=self._ownConfig["def_h"])
                    self.__canvas.set_up()
                    # self.__state.launch()
                    self.__current_state_name = current_state
                    # self.__gui.set_game_canvas()

            except Exception as exc:
                print(
                    "Can't import : {lib}".format(lib=class_name))
                print(
                    "Error message : {msg}".format(msg=exc.args))

    def add_msg_to_logger(self, msg):
        self.__canvas.add_msg_to_logger(msg=msg)
    ### GETTERS / SETTERS ###

    def getWidth(self):
        return self._ownConfig["def_w"]

    def getHeight(self):
        return self._ownConfig["def_h"]

    def set_game_canvas(self):
        self.__canvas = GameCanvas(self, self._ownConfig["def_w"], self._ownConfig["def_h"], gui=self,
                                   cfg=self._ownConfig["canvas"]["game"])
        self.__canvas.set_up()

    def get_grid(self):
        return self.__main.get_grid()

    def get_pieces(self):
        return self.__main.get_pieces()

    def set_stop_event(self):
        self._stopEvent.set()

    def get_window(self):
        return self.__window

    def ger_frame(self):
        return self.__canvas

    def get_buttons(self):
        return self.__canvas.get_buttons()

    def set_state(self, state):
        self.__main.set_state(state)

    def get_flash_msgs(self):
        return self.__main.get_flash_msgs()

    def get_theme(self):
        return self.__main.get_theme()

    def set_theme(self, theme):
        self.__main.set_theme(theme)

    def get_piece_color_choice(self, nb):

        if nb == 1:
            return self.__player_1_pieces_color
        else:
            return self.__player_2_pieces_color

    def set_player_pieces_img(self, nb, color):
        """
        Method to set up the pieces color of a layer
        -----------------------------------------------------------------------
        Arguments :
            - nb : Number of the player
            - color : String that represents the color
        -----------------------------------------------------------------------
        Return : None.
        """
        # Flag used to display a Flash Message
        no_change_color = False
        same_color_players = False
        color_changed = False

        # Checking the number
        if nb == 1:
            # Checking if we can change the color
            if self.__player_1_pieces_color == color:
                no_change_color = True
            elif self.__player_2_pieces_color == color:
                same_color_players = True
            else:
                self.__player_1_pieces_color = color
                color_changed = True

        else:
            if self.__player_2_pieces_color == color:
                no_change_color = True
            elif self.__player_1_pieces_color == color:
                same_color_players = True
            else:
                self.__player_2_pieces_color = color
                color_changed = True

        # Displaying Flash message that correspond to what happened
        if no_change_color:
            self.__main.add_flash_msg(
                FlashMessage(size=15, text="This player already have this color", x=0, y=0, code=INFO_CODE,
                             duration=2))

        elif same_color_players:
            self.__main.add_flash_msg(
                FlashMessage(size=15, text="Both players can't have the same color", x=0, y=0, code=INFO_CODE,
                             duration=2))

        elif color_changed:
            self.__main.add_flash_msg(
                FlashMessage(size=15, text="Color changed for player : " + self.int_to_string(nb), x=0, y=0, code=INFO_CODE,
                             duration=2))

    @staticmethod
    def int_to_string(number):
        if number == 1:
            return "one"
        elif number == 2:
            return "two"
        else:
            return "zero"

    def get_grid_choice(self):
        return self.__grid_choice

    def set_grid(self, grid):
        self.__grid_choice = grid
        self.__main.add_flash_msg(
            FlashMessage(size=15, text="Grid has been updated", x=0, y=0, code=INFO_CODE,
                         duration=2))

    def get_clickable_images(self):
        return self.__canvas.get_clickable_images()

    def get_strings(self):
        return self.__canvas.get_strings()


if __name__ == '__main__':
    pass
