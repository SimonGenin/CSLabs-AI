
from case import Case

class Agent:

    def __init__(self, texture, grid_x, grid_y):
        """
        :param texture: tuple with the image and the associate rect
        :param grid_x: the x position on the grid
        :param grid_y: the y position on the grid
        """
        self.texture = texture
        self.g_x = grid_x
        self.g_y = grid_y

    def draw(self, screen):

        # Set the image position
        self.texture[1].centerx = self.g_x * Case.pixel_size + Case.pixel_size // 2
        self.texture[1].centery = self.g_y * Case.pixel_size + Case.pixel_size // 2

        # render the image
        screen.blit(*self.texture)