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
from display.ClickableImage import ClickableImage
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
        # self.draw_title()
        self.draw_strings()
        self.draw_clickable_images()
        super(SettingsCanvas, self).draws()

    def set_up_title(self):
        # Font of the text.
        font = "res/font/GOOD_DADDY.otf"
        # Creating and setting up the text
        new_string = TextToDisp(font=font,
                                  size=30,
                                  text="Settings",
                                  x=100,
                                  y=100, color=(0, 0, 0))

        new_string.set_up()

        # Setting its x, y pos
        x = (self._width - new_string.getText().get_width()) / 2
        y = new_string.getText().get_height() - 10

        new_string.setX(x)
        new_string.setY(y)
        self._strings.append(new_string)

    def draw_bg(self):
        """
        Method used to draw the background
        -----------------------------------------------------------------------
        Arguments : None.
        -----------------------------------------------------------------------
        Return : None.
        """
        self.fill(self.__bg_color)


    def set_up(self):
        self.set_up_title()
        self.set_up_buttons()
        self.set_up_strings()
        self.set_up_clickable_images()


    def set_up_strings(self):

        """" SET UP CHOOSE GRID STRING """
        # Font of the text.
        font = "res/font/GOOD_DADDY.otf"
        # Creating and setting up the text
        new_str = TextToDisp(font=font,
                                  size=25,
                                  text="Choose a grid :",
                                  x=100,
                                  y=100, color=(0, 0, 0))

        new_str.set_up()

        # Setting its x, y pos
        x = (self._width - new_str.getText().get_width()) / 2
        y = new_str.getText().get_height() + 50

        new_str.setX(x)
        new_str.setY(y)

        self._strings.append(new_str)

        """" SET UP PLAYER 1 PIECE CHOOSE """
        # Font of the text.
        font = "res/font/GOOD_DADDY.otf"
        # Creating and setting up the text
        new_str = TextToDisp(font=font,
                             size=25,
                             text="Player one pieces :",
                             x=100,
                             y=100, color=(0, 0, 0))

        new_str.set_up()

        # Setting its x, y pos
        x = (self._width - new_str.getText().get_width()) / 2
        y = new_str.getText().get_height() + 180

        new_str.setX(x)
        new_str.setY(y)

        self._strings.append(new_str)

        """" SET UP PLAYER 2 PIECE CHOOSE """
        # Font of the text.
        font = "res/font/GOOD_DADDY.otf"
        # Creating and setting up the text
        new_str = TextToDisp(font=font,
                             size=25,
                             text="Player two pieces :",
                             x=100,
                             y=100, color=(0, 0, 0))

        new_str.set_up()

        # Setting its x, y pos
        x = (self._width - new_str.getText().get_width()) / 2
        y = new_str.getText().get_height() + 290

        new_str.setX(x)
        new_str.setY(y)

        self._strings.append(new_str)

    def set_up_clickable_images(self):
        """
        This method is used to set up clickable image. It will display to the
        user the differents grids and pieces available.
        -----------------------------------------------------------------------
        Arguments : None.
        -----------------------------------------------------------------------
        Return : None.
        """
        self.set_up_grids_img()
        self.set_up_pieces_img_p1()
        self.set_up_pieces_img_p2()

    def set_up_pieces_img_p1(self):
        x = 120
        y = 250
        new_img = ClickableImage(x=x, y=y, width=50, height=50, img_path="res/img/pieces/red/king.png",
                                 action=self.change_p1_pieces_red)
        new_img.set_up_img()
        self._clickable_images.append(new_img)

        x += 50+20
        new_img = ClickableImage(x=x, y=y, width=50, height=50, img_path="res/img/pieces/white/king.png",
                                 action=self.change_p1_pieces_white)
        new_img.set_up_img()
        self._clickable_images.append(new_img)

        x += 50 + 20
        new_img = ClickableImage(x=x, y=y, width=50, height=50, img_path="res/img/pieces/black/king.png",
                                 action=self.change_p1_pieces_black)
        new_img.set_up_img()
        self._clickable_images.append(new_img)

        x += 50 + 20
        new_img = ClickableImage(x=x, y=y, width=50, height=50, img_path="res/img/pieces/blue/king.png",
                                 action=self.change_p1_pieces_blue)
        new_img.set_up_img()
        self._clickable_images.append(new_img)

    def set_up_pieces_img_p2(self):
        x = 120
        y = 360
        new_img = ClickableImage(x=x, y=y, width=50, height=50, img_path="res/img/pieces/red/king.png",
                                 action=self.change_p2_pieces_red)
        new_img.set_up_img()
        self._clickable_images.append(new_img)

        x += 50+20
        new_img = ClickableImage(x=x, y=y, width=50, height=50, img_path="res/img/pieces/white/king.png",
                                 action=self.change_p2_pieces_white)
        new_img.set_up_img()
        self._clickable_images.append(new_img)

        x += 50 + 20
        new_img = ClickableImage(x=x, y=y, width=50, height=50, img_path="res/img/pieces/black/king.png",
                                 action=self.change_p2_pieces_black)
        new_img.set_up_img()
        self._clickable_images.append(new_img)

        x += 50 + 20
        new_img = ClickableImage(x=x, y=y, width=50, height=50, img_path="res/img/pieces/blue/king.png",
                                 action=self.change_p2_pieces_blue)
        new_img.set_up_img()
        self._clickable_images.append(new_img)


    def set_up_grids_img(self):

        x = 125
        y = 130
        new_img = ClickableImage(x=x, y=y, width=70, height=70, img_path="res/img/grids/chess_plate_1.png", action=self.change_grid_1)
        new_img.set_up_img()

        self._clickable_images.append(new_img)

        x += 70 + 20
        new_img = ClickableImage(x=x, y=y, width=70, height=70, img_path="res/img/grids/chess_plate_2.png",
                                 action=self.change_grid_2)
        new_img.set_up_img()

        self._clickable_images.append(new_img)

        x += 70 + 20
        new_img = ClickableImage(x=x, y=y, width=70, height=70, img_path="res/img/grids/chess_plate_3.png",
                                 action=self.change_grid_3)
        new_img.set_up_img()

        self._clickable_images.append(new_img)

    def draw_clickable_images(self):
        for img in self._clickable_images:
            self.blit(img.get_img(), (img.get_x(), img.get_y()))

    def set_up_buttons(self):
        bw, bh = 170,40

        # Creating and settign up first button :
        button = Button(x=0, y=0, width=bw, height=bh, color=(0, 0, 0), text="Home", master=self,
                        action=self.set_home_state)

        x = (self.get_width() - bw) / 2
        y = self.get_height() - 80
        button.set_x(x)
        button.setY(y)
        button.set_up()

        # Add it to the button list
        self._buttons.append(button)

    """
    ################################
        METHODS CALLED BY WIDGETS
    ################################
    """
    def change_grid_1(self):
        self._gui.set_grid(1)

    def change_grid_2(self):
        self._gui.set_grid(2)

    def change_grid_3(self):
        self._gui.set_grid(3)

    def set_home_state(self):
        self.set_state("home")

    def change_p1_pieces_red(self):
        self._gui.set_player_pieces_img(nb=1, color="red")

    def change_p1_pieces_blue(self):
        self._gui.set_player_pieces_img(nb=1, color="blue")

    def change_p1_pieces_white(self):
        self._gui.set_player_pieces_img(nb=1, color="white")

    def change_p1_pieces_black(self):
        self._gui.set_player_pieces_img(nb=1, color="black")

    def change_p2_pieces_red(self):
        self._gui.set_player_pieces_img(nb=2, color="red")

    def change_p2_pieces_white(self):
        self._gui.set_player_pieces_img(nb=2, color="white")

    def change_p2_pieces_black(self):
        self._gui.set_player_pieces_img(nb=2, color="black")

    def change_p2_pieces_blue(self):
        self._gui.set_player_pieces_img(nb=2, color="blue")



if __name__ == '__main__':
    pass
    