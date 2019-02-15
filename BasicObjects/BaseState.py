"""
    BaseState class
"""

# Module informations
__project__ = u''
__author__ = u'Pires Baptiste (baptiste.pires37@gmail.com)'
__date__ = u'01/02/19'
__version__ = u'1.0.0'


# Importations
from BasicObjects.BaseObject import BaseObject

# Specific definitions


# Classes / Functions declaration


class BaseState(BaseObject):
    """
    This class will be used as a base for all of the states.
    ---------------------------------------------------------------------------
    Attributes :
        - _main : Main object
        - _flash_msgs : List of FlashMessage objects
    """

    def __init__(self, cfg, main):
        """
        Constructor
        -----------------------------------------------------------------------
        Arguments :
        -----------------------------------------------------------------------
        Return : None.
        """
        super(BaseState, self).__init__(config=cfg)
        self._main = main
        self._flash_msgs = []

    def add_msg(self, msg):
        """
        Method used to add a FlashMessage
        -----------------------------------------------------------------------
        Arguments :
            - msh : [FlashMessage] FlashMessage object to add
        -----------------------------------------------------------------------
        Return : None.
        """
        self._flash_msgs.append(msg)

    def set_up(self):
        pass
    def launch(self):

        pass
    def handle_events(self, events):
        """
        Method description
        -----------------------------------------------------------------------
        Arguments :
        
        -----------------------------------------------------------------------
        Return : None.
        """
        pass

    def get_flash_msgs(self):
        """
        Method used to return all the flash messages of the state.
        -----------------------------------------------------------------------
        Arguments : None.
        -----------------------------------------------------------------------
        Return : self._flash_msgs : [list] List of FlashMessage objects
        """
        return self._flash_msgs


if __name__ == '__main__':
    pass
    