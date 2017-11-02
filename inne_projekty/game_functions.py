# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 22:45:23 2017

@author: Leszek
"""
import sys
import pygame

def check_events():
    '''Reakcja na zdarzenia generowane przez klawiaturę i mysz.'''
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
def update_screen(ai_settings, screen, ship):
    '''Uaktualnienie obrazow na ekranie i przejscie do nowego ekranu.'''
    # Odswieżenie ekranu w trakcie każdej iteracji pętli.
    screen.fill(ai_settings.bg_color)                        
    ship.blitme()
    
    # Wyswietlenie ostatnio zmodyfikowanego ekranu.
    pygame.display.flip()
