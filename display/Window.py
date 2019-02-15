"""
    Window object
"""

# Module informations
__project__ = u''
__author__ = u'Pires Baptiste (baptiste.pires37@gmail.com)'
__date__ = u''
__version__ = u'1.0.0'

# Importations
import tkinter as tk


# Specific definitions


# Classes / Functions declaration


class Window(object):
    """
    Window objects
    ---------------------------------------------------------------------------
    Attributes :
        - __window : tk.Tk() object
    """

    def __init__(self):
        """
        Constructor
        -----------------------------------------------------------------------
        Arguments :
        -----------------------------------------------------------------------
        Return : None.
        
        """
        self.__window = None

    def init(self):
        """
        Method used to create the window
        -----------------------------------------------------------------------
        Arguments : None.
        -----------------------------------------------------------------------
        Return : None.
        """
        self.__window = tk.Tk()

if __name__ == '__main__':
    pass
