"""
    This class is the main class, it will be used has a bridge for
    the GUI and the game logic.
"""

# Module informations
__project__ = u'Chess'
__author__ = u'Pires Baptiste (baptiste.pires37@gmail.com)'
__date__ = u'27/01/2019'
__version__ = u'1.0.0'

# Importations
from json import load
from display.GUI import GUI
from states.GameState import GameState
from importlib import import_module
from pygame import init

# Specific definitions
IMG_PATH = "res/img"


# Classes / Functions declaration


class Main(object):
    """
    This class is the main class, it will be used has a bridge for
    the GUI and the game logic.
    ---------------------------------------------------------------------------
    Attributes :
        - __allConfig : The whole configuration of the app
        - __gui : GUI object from the display package
        - __state : State object, can be home, game or any other state that will come soon
    """

    def __init__(self):
        """
        Constructor
        -----------------------------------------------------------------------
        Arguments : None.
        -----------------------------------------------------------------------
        Return : None.
        """
        super(Main, self).__init__()
        self.__allConfig = None
        self.__gui = None
        self.__state = None
        self.__current_state = ""
        self.__theme = 1
        init()

    def set_up(self):
        """
        This method is used to set up everything at the start of the game
        -----------------------------------------------------------------------
        Arguments : None.
        -----------------------------------------------------------------------
        Return : None.
        """
        # Loading the general config of the game
        self.load_config()

        # Setting the first state of the game to home
        self.set_state("home")
        self.__current_state = "home"
        # Loading GUI
        self.__gui = GUI(self.__allConfig["gui"], self)

    def launch(self):
        """
        This method is called to launch the app
        -----------------------------------------------------------------------
        Arguments : None.
        -----------------------------------------------------------------------
        Return : None.
        """
        self.__gui.start()

    def load_config(self):
        """
        This method load the configuration from the ./config.json file
        -----------------------------------------------------------------------
        Arguments : None.
        -----------------------------------------------------------------------
        Return : None.
        """
        cfg_file = open("./config.json")
        self.__allConfig = load(cfg_file, encoding='utf-8')
        cfg_file.close()

    def launch_game(self):
        """
        If this method is called, it will change the state of the game to
        GameState
        -----------------------------------------------------------------------
        Arguments : None.
        -----------------------------------------------------------------------
        Return : None.
        """
        # Game
        self.__state = GameState(self.__allConfig["game"], self)
        self.__state.launch()

    # GETTERS SETTERS

    def set_state(self, new_state):
        """
        This method is used to set_up the state from a str
        -----------------------------------------------------------------------
        Arguments : 
            - new_state : [str] Name of the state to instantiate
        -----------------------------------------------------------------------
        Return : None.
        """
        # Setting up the class name
        class_name = new_state.capitalize() + "State"

        # There we check if the current state is not the same
        if type(self.__state).__name__ != class_name:
            # Creating dynamically the state class
            try:
                # Import library
                module = import_module("states." + class_name)

                if class_name:
                    state_class = getattr(module, class_name)
                    # Setting the current state got in parameters as the new state
                    self.__state = state_class(main=self, cfg=self.__allConfig["states"][new_state.lower()])
                    self.__state.set_up()
                    self.__state.launch()
                    # self.__gui.set_game_canvas()
                    self.__current_state = new_state

            except Exception as exc:
                print(
                    "Can't import : {lib}".format(lib=class_name))
                print(
                    "Error message : {msg}".format(msg=exc.args))

    def get_current_state(self):
        return self.__current_state

    def get_grid(self):
        """
        This method return a list that is a grid
        -----------------------------------------------------------------------
        Arguments : None.
        -----------------------------------------------------------------------
        Return : self.__state.getGrid() [list]
        """
        return self.__state.get_grid()

    def get_buttons(self):
        """
        This method is used to get the buttons that are displayed by the GUI
        -----------------------------------------------------------------------
        Arguments : None.
        -----------------------------------------------------------------------
        Return : self.__gui.getButtons() [list]
        """
        return self.__gui.get_buttons()

    def set_canvas(self, state):
        """
        This method will be used to set up the canvas displayed by the GUI
        but atm it need to be fixed.
        -----------------------------------------------------------------------
        Arguments :
            - state [str] : str that is the name of the next canvas.
        -----------------------------------------------------------------------
        Return : None.
        """
        self.__gui.set_game_canvas()

    def get_pieces(self):
        """
        This method return all the pieces from a state object
        -----------------------------------------------------------------------
        Arguments : None.
        -----------------------------------------------------------------------
        Return : self.__state.getPieces() [list]
        """
        return self.__state.get_pieces()

    def handle_events(self, events):
        """
        This method is used to make the state handle events from the GUI.
        -----------------------------------------------------------------------
        Arguments : None.
        -----------------------------------------------------------------------
        Return : None.
        """
        if self.__state != None:
            self.__state.handle_events(events)

    def stop_gui(self):
        """
        Mehtod to stop the GUI. It set the stop event of the thread.
        -----------------------------------------------------------------------
        Arguments : None.
        -----------------------------------------------------------------------
        Return : None.
        """
        self.__gui.set_stop_event()

    def get_state(self):
        """
        Method to get the state
        -----------------------------------------------------------------------
        Arguments : None.
        -----------------------------------------------------------------------
        Return : self.__state [State Object]
        """
        return self.__state

    def get_flash_msgs(self):
        """
        This method is used to get the flash message that the state need to
        display
        -----------------------------------------------------------------------
        Arguments : None.
        -----------------------------------------------------------------------
        Return : self.__state.get_flash_msgs() [list]
        """
        return self.__state.get_flash_msgs()

    def get_theme(self):
        return self.__theme

    def set_theme(self, theme):
        if self.__theme != theme:
            self.__theme = theme
            print(self.__theme)

    def get_piece_color_choice(self, nb):
        return self.__gui.get_piece_color_choice(nb)

    def get_clickable_images(self):
        return self.__gui.get_clickable_images()

    def get_strings(self):
        return self.__gui.get_strings()

    def add_flash_msg(self, msg):
        self.__state.add_msg(msg=msg)

    def add_msg_to_logger(self, msg):
        self.__gui.add_msg_to_logger(msg)
if __name__ == '__main__':
    main = Main()
    main.set_up()
    main.launch()
