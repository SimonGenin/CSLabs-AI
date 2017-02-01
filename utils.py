import pygame

from case import Case


def prepare_texture(resource):
    """
    Prepare a tuple for the texture.
    It is this format that is used for the draw operations.
    :param resource: path to the image (png, jpg)
    :return tuple with raw image and rect
    """
    global tex
    image = pygame.image.load(resource)
    image = pygame.transform.scale(image, (Case.pixel_size, Case.pixel_size))
    image_rect = image.get_rect()
    return image, image_rect
