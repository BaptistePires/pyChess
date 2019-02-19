"""
    Class for #decrisption de la class
"""

# Module informations
__project__ = u''
__author__ = u'Pires Baptiste (baptiste.pires37@gmail.com)'
__date__ = u''
__version__ = u'1.0.0'


# Importations


# Specific definitions


# Classes / Functions declaration


class BaseWidget(object):
    """
    Class description
    ---------------------------------------------------------------------------
    Attributes :

        - x : x position
        - y : y position
        - width : width of the widget
        - height : height of the widget
        - action : action to do when the widget is clicked
    """

    def __init__(self, x, y, width, height, action=None):
        """
        Constructor
        -----------------------------------------------------------------------
        Arguments : See attributes above.
        -----------------------------------------------------------------------
        Return : None.
        """
        super(BaseWidget, self).__init__()
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._action = action


    def hover(self, mx, my):
        """
        Method called when the mouse is over the widget
        -----------------------------------------------------------------------
        Arguments :
            - mx : mouse x position
            - my : mouse y position
        -----------------------------------------------------------------------
        Return : None.
        """
        pass

    def action(self):
        """
        Method used to call the function/method when the widget is clicked
        -----------------------------------------------------------------------
        Arguments : See attributes above.
        -----------------------------------------------------------------------
        Return : None.
        """
        if self._action is not None:
            self._action()


    ### GETTERS / SETTERS ###

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height

    def set_x(self, x):
        self._x = x

    def setY(self, y):
        self._y = y



if __name__ == '__main__':
    pass
    