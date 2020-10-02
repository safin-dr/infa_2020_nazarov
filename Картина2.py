import pygame
from pygame.draw import *
import numpy as np

#Список используемых цветов

SKY = (85, 213, 255)
CLOUD = (255, 255, 255)
SUN = (249, 194, 194)
BLACK = (0, 0, 0)
LEAVES = (12, 96, 12)
GREEN = (19, 155, 19)
HOUSE = (137, 109, 39)
WINDOW = (139, 183, 197)
FRAME = (150, 2, 2)
ROOF = (207, 42, 42)

#Задаём массив для построения листвы деревьев

CORDS = [[5, 55], [25, 35], [-15, 35], [5, 25], [-12, 10], [22, 8]]
r_leafs = 20	

#Задаем необходимые функции

def circle_with (x_c, y_c, R_c, COLOR):
	'''
	Функция рисует круг с черной обводной
	x_c, y_c - координаты центра круга
	R_c - радиус круга
	COLOR - цвет круга, заданный в формате, подходящем для pygame.Color
	'''
	circle(screen, BLACK, (x_c, y_c), R_c + 1)
	circle(screen, COLOR, (x_c, y_c), R_c)
	
def house(h_x, h_y, h_height, h_length):
	'''
	Функция рисует дом с окошком и обводкой
	h_x, h_y - координаты левого верхнего угла изображения
	h_height - высота изображения
	h_length - длина изображения
	'''
	window_len = round (0.25 * h_length )
	wingow_height = round (0.33 * h_height )
	w_x = h_x + round (0.375 * h_length )
	w_y = h_y + round (0.33 * h_height )
	rect(screen, HOUSE, (h_x, h_y, h_length, h_height))
	rect(screen, BLACK, (h_x, h_y, h_length, h_height), 2)
	rect(screen, WINDOW, (w_x, w_y, window_len, wingow_height))
	rect(screen, FRAME, (w_x, w_y, window_len, wingow_height), 2)
	polygon(screen, ROOF, [(h_x, h_y), (h_x + h_length, h_y), 
		(h_x + round(0.5 * h_length), h_y - round(0.5 * h_height))]) 
	polygon(screen, BLACK, [(h_x, h_y), (h_x + h_length, h_y), 
		(h_x + round(0.5 * h_length), h_y - round(0.5 * h_height))], 2)

def cloud(R, x_cl, y_cl):
	'''
	Функция рисует облако 
	x_cl, y_cl - координаты середины левого нижнего круга
	R - радиус круга
	'''
	for i in range(4):
		circle_with(x_cl + R * i, y_cl, R, CLOUD)
	for i in range(2):
		circle_with(x_cl + (2 - i) * R, y_cl - R, R, CLOUD)

def tree(r_x, r_y, t_size, COLOR):
	'''
	Фунция рисует дерево
	r_x, r_y - координаты левого верхнего угла ствола 
	t_size - параметр, отвечающий за размер дерева
	COLOR - цвет листвы, заданный в формате, подходящем для pygame.Color
	'''
	rect(screen, BLACK, (r_x, r_y, 10 * t_size, 60 * t_size))
	for x in CORDS:
		circle_with(r_x + t_size * x[0], r_y - t_size * x[1], t_size * r_leafs, COLOR)
		

def draw_sun(x_sun, y_sun, R, S, r):
	'''
	Функция рисует Солнце с лучами и обводкой
	x_sun, y_sun - координаты центра изображения
	R - радиус круга
	S - количество
	r - длина луча 
	'''
	circle(screen, BLACK, (x_sun, y_sun), R + 1 , 3) 
	for i in range(S):
		polygon(screen, BLACK, [(x_sun + round( R * np.sin ( 2 * i * np.pi / S )), y_sun - round( R * np.cos (2 * i * np.pi / S ))),
		(x_sun + round( R * np.sin ( (2 * i + 1) * np.pi / S )), y_sun - round( R * np.cos ((2 * i + 1) * np.pi / S ))),
		(x_sun + round( (R + r) * np.sin ((2 * i + 0.5) * np.pi / S )), y_sun - round( (R + r) * np.cos ((2 * i + 0.5) * np.pi / S )))], 3)
		polygon(screen, SUN, [(x_sun + round( R * np.sin ( 2 * i * np.pi / S )), y_sun - round( R * np.cos (2 * i * np.pi / S ))),
		(x_sun + round( R * np.sin ( (2 * i + 1) * np.pi / S )), y_sun - round( R * np.cos ((2 * i + 1) * np.pi / S ))),
		(x_sun + round( (R + r) * np.sin ((2 * i + 0.5) * np.pi / S )), y_sun - round( (R + r) * np.cos ((2 * i + 0.5) * np.pi / S )))])	  
	circle(screen, SUN, (x_sun, y_sun), R)
	
	       
pygame.init()

FPS = 30
screen = pygame.display.set_mode((900, 500)) 

#Окрашивание неба и земли

rect(screen, SKY, (0, 0, 900, 250))
rect(screen, GREEN, (0, 250, 900, 250))

#Параметры Солнца

R = 30
S = 16
r = 5
x_sun = 50
y_sun = 40

#Рисование объектов
	
draw_sun(x_sun, y_sun, R, S, r)

cloud(24, 130, 70)
cloud(20, 430, 97)
cloud(25, 760, 84)	  

house(60, 270, 130, 180)
house(510, 268, 100, 160)

tree(400, 320, 2, LEAVES)
tree(760, 270, 1, LEAVES)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
