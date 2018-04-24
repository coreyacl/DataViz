

import Occupation_Research
import pygame, sys

import time
import os



import pygame

pygame.init()
background_colour = (255,255,255)

(width, height) = (1280, 960)

screen = pygame.display.set_mode((width, height))

screen.fill(background_colour)

myfont = pygame.font.SysFont('Comic Sans MS', 30)
textsurface = myfont.render(str(Occupation_Research.list_of_hashes[2]), False, (0, 0, 0))

screen.blit(textsurface,(0,0))
pygame.display.flip()
running = True
while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
