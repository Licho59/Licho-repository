# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 19:43:39 2017

@author: Leszek
"""
# pygame - kod wyswietlajÄ…cy kolejkÄ™ wiadomosci
import pygame
from pygame.locals import *
from sys import exit

pygame.init()
SCREEN_SIZE = (640, 480)
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)

font = pygame.font.SysFont("arial", 16)
font_height = font.get_linesize()
event_text = []

while True:
    
    event = pygame.event.wait()
    event_text.append(str(event))
    event_text = event_text[int(-SCREEN_SIZE[1]/font_height):]
    
    if event.type == QUIT:
       pygame.quit()
       exit()
        
    screen.fill((230, 230, 230))
    
    y = SCREEN_SIZE[1]-font_height
    for text in reversed(event_text):
        screen.blit(font.render(text, True, (0, 0, 0)), (0, y))
        y -= font_height
        
    pygame.display.update()
                   
