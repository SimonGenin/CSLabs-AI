import pygame

from agent import Agent
from board import Board
from utils import prepare_texture

background_colour = (255, 255, 255)
(width, height) = (800, 800)

# Make the window
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('CSLabs - AI')
screen.fill(background_colour)

# Refresh and show
pygame.display.flip()

b = Board(10, 10)

tex = prepare_texture("wall.jpg")
a = Agent(tex, 1, 0)

# Game loop
running = True
while running:

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    a.draw(screen)

    pygame.display.flip()

    pygame.time.wait(100)



