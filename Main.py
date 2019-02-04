"""
    Class for #decrisption de la class
"""

# Module informations
__project__ = u'Chess'
__author__ = u'Pires Baptiste (baptiste.pires37@gmail.com)'
__date__ = u'27/01/2019'
__version__ = u'1.0.0'


# Importations
import json
from display.GUI import GUI
from game.Game import Game
# Specific definitions
IMG_PATH = "res/img"

# Classes / Functions declaration


class Main(object):
    """
    Class description
    ---------------------------------------------------------------------------
    Attributes :
    
    """

    def __init__(self):
        """
        Constructor
        -----------------------------------------------------------------------
        Arguments :
        -----------------------------------------------------------------------
        Return : None.
        
        """
        super(Main, self).__init__()
        self.__allConfig = None
        self.__gui = None
        self.__grid = []
        self.__game = None

    def setUp(self):
        # Loading the general config of the game
        self.loadConfig()

        # Game
        self.__game = Game(self.__allConfig["game"], self)
        # Loading GUI, game, etc ...s
        self.__gui = GUI(self.__allConfig["gui"], self)



    def launch(self):
        # Launch sub classes and processes
        self.__game.launch()
        self.__gui.start()

    def loadConfig(self):
        cfg_file = open("./config.json")
        self.__allConfig = json.load(cfg_file, encoding='utf-8')
        cfg_file.close()


# GETTERS SETTERS

    def getGrid(self):
        return self.__game.getGrid()

    def getPieces(self):
        return self.__game.getPieces()

    def handle_events(self,events):
        self.__game.handle_events(events)

    def stop_gui(self):
        self.__gui.set_stop_event()

    def getGame(self):
        return self.__game

if __name__ == '__main__':
    main = Main()
    main.setUp()
    main.launch()
    