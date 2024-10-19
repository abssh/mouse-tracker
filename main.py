import pygame

from dragon.dragon import Dragon
from tracker import Tracker


pygame.init

screen = pygame.display.set_mode((0, 0))

pygame.display.set_caption("Mouse Tracker")
clock = pygame.time.Clock()
# font = pygame.font.SysFont('quicksand.ttf', 20)

dragon = Dragon(screen)


running = True
while running:
    screen.fill((242, 242, 242))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        
    dragon.update(*pygame.mouse.get_pos())

    pygame.display.flip()
    clock.tick(60)

        