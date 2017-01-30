import pygame

# Window options
background_colour = (255,255,255)
(width, height) = (300, 200)

# Make the window
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tutorial 1')
screen.fill(background_colour)

# Show the window
pygame.display.flip()

# Game loop
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False