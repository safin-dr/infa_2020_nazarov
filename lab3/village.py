import pygame
from pygame.draw import *
import random as r

def sun():
    circle(screen, (255, 255, 0), (r.randint(450, 900), r.randint(40, 120)), 25)
    
def house():
    h_x = r.randint(0, 200)
    h_y = r.randint(250, 300)
    h_height = r.randint(150, 200)
    h_length = r. randint(150, 250)
    window_len = 0.25 * h_length
    wingow_height = 0.33 * h_height
    w_x = h_x + 0.375*h_length
    w_y = h_y + 0.33*h_height
    rect(screen, (255, 100, 100), (h_x, h_y, h_length, h_height))
    rect(screen, (15, 169, 45), (h_x, h_y, h_length, h_height), 5)
    rect(screen, (40, 40, 40), (w_x, w_y, window_len, wingow_height))
    rect(screen, (0, 0, 0), (w_x, w_y, window_len, wingow_height), 2)
    polygon(screen, (200, 100, 255), [(h_x, h_y), (h_x + h_length, h_y), (h_x + 0.5*h_length, h_y - 0.33*h_height)]) 
    polygon(screen, (255, 0, 0), [(h_x, h_y), (h_x + h_length, h_y), (h_x + 0.5*h_length, h_y - 0.33*h_height)], 3)

def cloud():
    length = r.randint(0, 600)
    for i in range (round(0.09 * length)):
        randx = (r.randint(r.randint(350, 550) - round(0.5*length) , r.randint(350, 550) + round(0.5*length))) 
        randy = r.randint(40, 140)
        randr = r.randint(30, 80)
        randwhite = r.randint(235, 255)
        circle(screen, (randwhite, randwhite, randwhite), (randx , randy), randr)
        i += 1

def tree(n):
    for i in range(n):
        height = r.randint(65, 155)
        width = r.randint(10, 15)
        roots_x = r.randint(450, 900)
        roots_y = r.randint(275, 375)
        rect(screen, (139, 71, 80), (roots_x, roots_y, width, height))
        leaves = r.randint(3, 5)
        for k in range(leaves):
            circle(screen, (0, r.randint(150, 175), 0), (roots_x + r.randint(-30, 30), roots_y + r.randint(-30, 30)), r.randint(35, 45))
            k += 1
        i += 1
        


pygame.init()

FPS = 30
screen = pygame.display.set_mode((900, 500)) 

rect(screen, (50, 50, 255), (0, 0, 900, 250))
rect(screen, (50, 255, 100), (0, 250, 900, 250))


n = int(input())


sun()
tree(n)
cloud()
house()




pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
