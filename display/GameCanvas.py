"""
    Class for #decrisption de la class
"""

# Module informations
__project__ = u''
__author__ = u'Pires Baptiste (baptiste.pires37@gmail.com)'
__date__ = u''
__version__ = u'1.0.0'

# Importations
import pygame

# Specific definitions


# Classes / Functions declaration


class GameCanvas(pygame.Surface):
    """
    Class description
    ---------------------------------------------------------------------------
    Attributes :
    
    """

    def __init__(self, master, width, height, gui):
        """
        Constructor
        -----------------------------------------------------------------------
        Arguments :
        -----------------------------------------------------------------------
        Return : None.
        
        """
        super(GameCanvas, self).__init__(size=(width, height))
        self.__width = width
        self.__height = height
        self.__gui = gui
        self.__case_size = 62.5
        self.__labels = []
        self.__master = master
        self.__bg_img = None


    def draws(self):
        """
        Method used to draw all images needed
        -----------------------------------------------------------------------
        Arguments :
        
        -----------------------------------------------------------------------
        Return :
            None
        """
        # self.fill((255, 255, 255))
        self.draw_grid()
        self.draw_entities()

    def set_up(self):
        """
        Setting up the images and everything else
        :return:
        """
        self.set_up_entites_img()
        self.set_up_bc_img()

    def set_up_bc_img(self):
        """
        Method used to load background image
        :return:
        """
        img = pygame.image.load("res/img/echiquier.png")
        self.__bg_img = pygame.transform.scale(img, (self.__gui.getWidth(), self.__gui.getHeight()))

    def set_up_entites_img(self):
        """
        Method used to load entities img
        :return:
        """
        for p_player in self.__gui.getPieces():
            for  piece in p_player:
                piece.set_img()

    def draw_entities(self):
        """
        Method used to draw all entities
        :return:
        """
        players_pieces = self.__gui.getPieces()

        for p_player in players_pieces:
            for i, piece in enumerate(p_player):
                if piece.is_alive():
                    # img = pygame.image.load(piece.getImgPath())
                    # img = pygame.transform.scale(img, (int(self.__case_size - 15), int(self.__case_size - 15)))
                    if not piece.is_selected():
                        if piece.getY() > 5:
                            y = int(piece.getY()) * self.__case_size + int(15 / 2)
                        else:
                            y = piece.getY() * self.__case_size + int(15 / 2)
                        x = int(piece.getX() * self.__case_size) + int(15 / 2)
                        self.blit(piece.getImg(), (x, y))
                    else:

                        # print(piece.getImg())
                        self.blit(piece.getImg(), (
                        int(pygame.mouse.get_pos()[0] - (62.5 / 2)), int(pygame.mouse.get_pos()[1] - (62.5 / 2))))

    def draw_grid(self):
        """
        Method used to draw the grid (before it was drawn with lines, now it's an image, it use less ressources)
        :return:
        """
        self.blit(self.__bg_img, (0, 0))
        # self.__case_size = int(self.__width) / len(grid)

        #         pygame.draw.line(self, (0, 0, 0), ((j * self.__case_size), (i * self.__case_size)),
        #                          ((j * self.__case_size), i * self.__case_size))
        #         pygame.draw.line(self, (0, 0, 0), ((j * self.__case_size), self.__case_size + (i * self.__case_size)),
        #                          ((j * self.__case_size) + self.__case_size, self.__case_size + (i * self.__case_size)))
        #         pygame.draw.line(self, (0, 0, 0), ((j * self.__case_size), self.__case_size + (i * self.__case_size)),
        #                          ((j * self.__case_size), i * self.__case_size))

        # self.disp_case_i(self.__gui.getGrid())


    def disp_case_i(self, grid):
        """
        Method used to draw squares indexes on the screen used for debug because it use a lot of ressources
        :param grid:
        :return:
        """
        for i in grid:
            for j in range(8):
                myfont = pygame.font.SysFont("monospace", 15)
                # render text
                label = myfont.render("[" + str(j) + ";" + str(i) + ']', 1, (0, 0, 0))
                self.blit(label, ((j * self.__case_size) + 7, (i * self.__case_size) + 7))


if __name__ == '__main__':
    pass
