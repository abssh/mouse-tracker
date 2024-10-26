import pygame

from colors import Colors
from worm.worm import Worm

pygame.init()

screen = pygame.display.set_mode((0, 0))

pygame.display.set_caption("Mouse Tracker")
clock = pygame.time.Clock()
# font = pygame.font.SysFont('quicksand.ttf', 20)

worm = Worm(screen)

running = True
while running:
    screen.fill(Colors.Scary)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

    worm.update(*pygame.mouse.get_pos())

    pygame.display.flip()
    clock.tick(80)
