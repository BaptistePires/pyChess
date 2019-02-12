"""
    Class for #decrisption de la class
"""

# Module informations
__project__ = u''
__author__ = u'Pires Baptiste (baptiste.pires37@gmail.com)'
__date__ = u''
__version__ = u'1.0.0'


# Importations
from display.TextToDisp import TextToDisp

# Specific definitions
INFO_CODE = 0
WARNING_CODE = 1
DANGER_CODE = 2

# Classes / Functions declaration

class FlashMessage(TextToDisp):
    """
    Class description
    ---------------------------------------------------------------------------
    Attributes :
    
    """

    def __init__(self, size, text, x, y, code, color=None, font="res/font/Montserrat-Regular.ttf", duration=1):
        """
        Constructor
        -----------------------------------------------------------------------
        Arguments :
        -----------------------------------------------------------------------
        Return : None.
        """
        super(FlashMessage, self).__init__(font, size, text, x, y, color)
        self.__code = code
        self.__first_display = 0
        self.__font = font
        self.__duration = duration

    def get_color_by_code(self):
        """
        Method description
        -----------------------------------------------------------------------
        Arguments :
        
        -----------------------------------------------------------------------
        Return : None.
        """

        if self.__code == INFO_CODE:
            return (25,25,112)
        elif self.__code == WARNING_CODE:
            return 	(255,215,0)
        elif self.__code == DANGER_CODE:
            return (0,0,0)

    def getDuration(self):
        return self.__duration

    def getColor(self):
        return self.get_color_by_code()

    def get_code(self):
        return self.__code

    def get_first_display(self):
        return self.__first_display

    def set_first_display(self, first_disp):
        self.__first_display = first_disp

    def get_font(self):
        return self.__font

if __name__ == '__main__':
    pass
    