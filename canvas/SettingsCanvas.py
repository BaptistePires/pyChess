"""
    Class for #decrisption de la class
"""

# Module informations
__project__ = u''
__author__ = u'Pires Baptiste (baptiste.pires37@gmail.com)'
__date__ = u''
__version__ = u'1.0.0'


# Importations
from BasicObjects.BaseCanvas import BaseCanvas
from display.TextToDisp import TextToDisp
from display.Button import Button
# Specific definitions


# Classes / Functions declaration


class SettingsCanvas(BaseCanvas):
    """
    Class description
    ---------------------------------------------------------------------------
    Attributes :
    
    """

    def __init__(self, cfg, master, gui, height, width):
        """
        Constructor
        -----------------------------------------------------------------------
        Arguments :
        -----------------------------------------------------------------------
        Return : None.
        """
        super(SettingsCanvas, self).__init__(cfg=cfg, master=master, gui=gui, height=height, width=width)
        self.__bg_color = (255, 255, 255)
        self.__title = None



    def draws(self):
        self.draw_bg()
        self.draw_buttons()


    def set_up_title(self):
        # Font of the text.
        font = "res/font/good_time.ttf"
        # Creating and setting up the text
        self.__title = TextToDisp(font=font,
                                  size=30,
                                  text="Settings",
                                  x=100,
                                  y=100, color=(0, 0, 0))

        self.__title.set_up()

        # Setting its x, y pos
        x = (self._width - self.__title.getText().get_width()) / 2
        y = self.__title.getText().get_height()

        self.__title.setX(x)
        self.__title.setY(y)

    def draw_bg(self):
        """
        Method used to draw the background
        -----------------------------------------------------------------------
        Arguments : None.
        -----------------------------------------------------------------------
        Return : None.
        """
        self.fill(self.__bg_color)
        self.draw_title()

    def draw_title(self):
        """
        Method used to draw the title on the canvas.
        -----------------------------------------------------------------------
        Arguments : None.
        -----------------------------------------------------------------------
        Return : None.
        """
        self.blit(self.__title.getText(),
                  (self.__title.getX(), self.__title.getY()))

    def set_up(self):
        self.set_up_title()
        self.set_up_buttons()

    def set_up_buttons(self):
        bw, bh = 170,40

        # Creating and settign up first button :
        button = Button(x=0, y=0, w=bw, h=bh, color=(0, 0, 0), text="Home", master=self,
                        action=self.set_home_state)

        x = (self.get_width() - bw) / 2
        y = self.get_height() - 80
        button.setX(x)
        button.setY(y)
        button.set_up()

        # Add it to the button list
        self._buttons.append(button)

        button = Button(x=80, y=100, w=100, h=40, color=(0,0,0), text="Theme 1", master=self, action=self.change_theme_to_1)
        button.set_up()
        self._buttons.append(button)

        button = Button(x=200, y=100, w=100, h=40, color=(0,0,205), text="Theme 2", master=self, action=self.change_theme_to_2)
        button.set_up()
        self._buttons.append(button)

        button = Button(x=320, y=100, w=100, h=40, color=(34,139,34), text="Theme 2", master=self, action=self.change_theme_to_2)
        button.set_up()
        self._buttons.append(button)


        x = (self.get_width() - 150) / 2
        y =180
        button = Button(x=x, y=y, w=150, h=60, color=(0,0,0), text="music", master=self,
                        action=self.change_theme_to_2)
        button.set_up()
        self._buttons.append(button)

        x = (self.get_width() - 150) / 2
        y = 260
        button = Button(x=x, y=y, w=150, h=60, color=(0, 0, 0), text="Credit", master=self,
                        action=self.change_theme_to_2)
        button.set_up()
        self._buttons.append(button)

    def change_theme_to_1(self):
        pass

    def change_theme_to_2(self):
        pass
    def set_home_state(self):
        self.set_state("home")
if __name__ == '__main__':
    pass
    