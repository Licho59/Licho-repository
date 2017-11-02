# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 20:41:20 2017

@author: Leszek
"""

import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    '''Klasa przedstawiająca pojedynczą gwiazdę.'''
    
    def __init__(self, stars_settings, screen):
        '''Inicjalizacja gwiazdy i zdefiniowanie jej położenia początkowego.'''
        super(Star, self).__init__()
        self.screen = screen
        self.stars_settings = stars_settings
        
        # Wczytanie gwiazdy i zdefiniowanie jego atrybutu rect.
        self.image = pygame.image.load('images/star.bmp')
        self.rect = self.image.get_rect()
        
        # Umieszczenie nowej gwiazdy w pobliżu lewego górnego rogu ekranu.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # Przechowywanie dokładnego położenia obcego.
        self.x = float(self.rect.x)
        
    def blitme(self):
        '''Wyswietlenie gwiazdy w jej aktualnym położeniu.'''
        self.screen.blit(self.image, self.rect)
        
#==============================================================================
#     def check_edges(self):
#         '''Zwraca wartosć True, jesli obcy znajduje się przy krawędzi ekranu'''
#         screen_rect = self.screen.get_rect()
#         if self.rect.right >= screen_rect.right:
#             return True
#         elif self.rect.left <= 0:
#             return True
#==============================================================================

    def update(self):
        '''Przesunięcie gwiazdy w prawo lub w lewo.'''
        self.x += (self.stars_settings.star_speed_factor *
                           self.stars_settings.fleet_direction)
        self.rect.x = self.x