"""
    HomeState class
"""

# Module informations
__project__ = u''
__author__ = u'Pires Baptiste (baptiste.pires37@gmail.com)'
__date__ = u''
__version__ = u'1.0.0'

# Importations
from BasicObjects.BaseState import BaseState
import pygame


# Specific definitions


# Classes / Functions declaration


class HomeState(BaseState):
    """
    This is the HomeState of the game
    ---------------------------------------------------------------------------
    Attributes :
        See BaseState class.
    """

    def __init__(self, cfg, main):
        """
        Constructor
        -----------------------------------------------------------------------
        Arguments : See BaseState class.
        -----------------------------------------------------------------------
        Return : None.
        """
        super(HomeState, self).__init__(cfg=cfg, main=main)

    def handle_events(self, events):
        """
        This method is used to handle events from the GUI.
        -----------------------------------------------------------------------
        Arguments :
            - events : event list from the GUI.
        -----------------------------------------------------------------------
        Return : None.
        """

        # We go through all events
        for e in events:

            if e.type == pygame.QUIT:
                self._main.stop_gui()

            elif e.type == pygame.MOUSEBUTTONUP:  # Event when the mouse button is released
                mx, my = pygame.mouse.get_pos()

                # We check if there is a button under the click
                for widget in self._main.get_buttons() + self._main.get_clickable_images():
                    if mx > widget.get_x() and mx < widget.get_x() + widget.get_width() and my > widget.get_y() and my < widget.get_y() + widget.get_height():
                        widget.action()
            else:
                mx, my = pygame.mouse.get_pos()
                for widget in self._main.get_buttons():
                    widget.hover(mx, my)

    def launch(self):
        pass

    def set_up(self):
        pass


if __name__ == '__main__':
    pass
