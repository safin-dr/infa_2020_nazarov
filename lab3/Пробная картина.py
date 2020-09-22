import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 600)) 

rect(screen, (255, 255, 255), (0, 0, 600, 600))

circle(screen, (0, 255, 50), (300, 300), 250)
circle(screen, (255, 100, 0), (200, 200), 60)
circle(screen, (100, 0, 255), (400, 200), 60)
circle(screen, (155, 90, 0), (400, 200), 30)
circle(screen, (0, 0, 255), (200, 200), 30)
rect(screen, (200, 100, 100), (200, 400, 200, 50))
rect(screen, (0, 0, 0), (200, 415, 200, 20))
polygon(screen, (50, 50, 50), [(80,70), (250,110),
                               (230,130), (60,100)])
polygon(screen, (50, 50, 50), [(520,70), (350,110),
                               (370,130), (540,100)])
polygon(screen, (30, 30, 100), [(300,220), (265,365),
                               (335,365)])




pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
