"""
    Setting stae class
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


class SettingsState(BaseState):
    """
    Setting state class
    ---------------------------------------------------------------------------
    Attributes :
        See super class.
    """

    def __init__(self, cfg, main):
        """
        Constructor
        -----------------------------------------------------------------------
        Arguments : See super class.
        -----------------------------------------------------------------------
        Return : None.
        """
        super(SettingsState, self).__init__(cfg=cfg, main=main)


    def handle_events(self, events):
        """
        See super class.
        -----------------------------------------------------------------------
        Arguments : See super class.
        -----------------------------------------------------------------------
        Return : See super class.
        """
        super(SettingsState, self).handle_events(events=events)
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
                for widget in self._main.get_buttons() + self._main.get_clickable_images():
                    widget.hover(mx, my)


if __name__ == '__main__':
    pass
    