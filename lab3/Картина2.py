import pygame
from pygame.draw import *
import random as r

n = 1

def sun():
    circle(screen, (255, 255, 0), (r.randint(750, 830), r.randint(40, 120)), 35)
    
def house_1():
    h_x = r.randint(0, 100)
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
    
def house_2():
    h_x = r.randint(400, 450)
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

def cloud_2():
    length = r.randint(0, 200)
    for i in range (round(0.15 * length)):
        randx = r.randint(500, 700)
        randy = r.randint(40, 140)
        randr = r.randint(30, 80)
        randwhite = r.randint(225, 255)
        circle(screen, (randwhite, randwhite, randwhite), (randx , randy), randr)
        i += 1
        
def cloud_1():
    length = r.randint(0, 200)
    for i in range (round(0.15 * length)):
        randx = r.randint(100, 200)
        randy = r.randint(40, 140)
        randr = r.randint(30, 80)
        randwhite = r.randint(225, 255)
        circle(screen, (randwhite, randwhite, randwhite), (randx , randy), randr)
        i += 1

def tree_1(n):
    for i in range(n):
        height = r.randint(100, 200)
        width = r.randint(10, 15)
        roots_x = r.randint(300, 350)
        roots_y = r.randint(275, 375)
        rect(screen, (139, 71, 80), (roots_x, roots_y, width, height))
        leaves = r.randint(15, 25)
        for k in range(leaves):
            circle(screen, (0, r.randint(150, 175), 0), (roots_x + r.randint(-30, 30), roots_y + r.randint(-30, 30)), r.randint(45, 55))
            k += 1
        i += 1

def tree_2(n):
    for i in range(n):
        height = r.randint(100, 200)
        width = r.randint(10, 15)
        roots_x = r.randint(700, 800)
        roots_y = r.randint(275, 375)
        rect(screen, (139, 71, 80), (roots_x, roots_y, width, height))
        leaves = r.randint(15, 25)
        for k in range(leaves):
            circle(screen, (0, r.randint(150, 175), 0), (roots_x + r.randint(-30, 30), roots_y + r.randint(-30, 30)), r.randint(45, 55))
            k += 1
        i += 1
        
pygame.init()

FPS = 30
screen = pygame.display.set_mode((900, 500)) 

rect(screen, (50, 50, 255), (0, 0, 900, 250))
rect(screen, (50, 255, 100), (0, 250, 900, 250))

sun()
tree_1(n)
tree_2(n)
cloud_1()
cloud_2()
house_1()
house_2()

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
