"""
    BaseProcess class
"""

# Module informations
__project__ = u''
__author__ = u'Pires Baptiste (baptiste.pires37@gmail.com'
__modifiers__ = u''
__date__ = u''
__version__ = u'1.0.0'


# Importations
# Multiprocessing library
from multiprocessing import Process, Event


# Specific definitions


# Classes / Functions declaration


class MyBaseProcess(Process):
    """
    Base process class for all the process in the game
    ---------------------------------------------------------------------------
    Attributes :
        - _own_config : Self configuration of the object
        - _is_running  : True when the process is running.
        - _stopEvent : Event used to stop the process.
    """

    def __init__(self, config):
        """
        Constructor
        -----------------------------------------------------------------------
        Arguments :
            - config : Config of the class
        -----------------------------------------------------------------------
        Return : None.
        """

        # Initalize attributes
        self._ownConfig = config
        self._isRunning = False
        self._stopEvent = Event()

        # Calling mother class
        super(MyBaseProcess, self).__init__()


    def before_processing(self):
        """
        Method called before processing
        -----------------------------------------------------------------------
        Arguments : None.
        -----------------------------------------------------------------------
        Return : None.
        """
        pass


    def after_processing(self):
        """
        Method called before processing
        -----------------------------------------------------------------------
        Arguments : None.
        -----------------------------------------------------------------------
        Return : None.
        """
        pass

    def handle_self_events(self):
        """
        Method called by the process to handle his events.
        -----------------------------------------------------------------------
        Arguments : None.
        -----------------------------------------------------------------------
        Return : None.
        """
        # Check if the process needs to stop
        if self._stopEvent.is_set():
            self._isRunning = False