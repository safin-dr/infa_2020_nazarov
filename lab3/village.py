import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((1800, 1000)) 

rect(screen, (100, 100, 255), (0, 0, 1800, 500))
rect(screen, (50, 255, 50), (0, 500, 1800, 500))

rect(screen, (50, 75, 50), (100, 400, 400, 200))
rect(screen, (0, 0, 0), (100, 400, 400, 200), 2)
polygon(screen, (30, 30, 100), [(100, 400), (500,400),
                               (300,300)])
rect(screen, (200, 200, 255), (250, 450, 100, 75))
rect(screen, (0, 0, 0), (250, 450, 100, 75), 2)

rect(screen, (0, 0, 0), (1400, 400, 30, 300))
circle(screen, (0, 100, 0), (1400, 410), 50)
circle(screen, (0, 90, 0), (1415, 390), 50)
circle(screen, (0, 100, 0), (1425, 380), 50)
circle(screen, (0, 90, 0), (1385, 405), 50)
circle(screen, (0, 100, 0), (1375, 395), 50)





pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
