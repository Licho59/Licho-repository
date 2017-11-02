# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 17:16:04 2017

@author: Ja
"""

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''Klasa przeznaczona do zarządzania pociskami wystrzeliwanymi przez state.'''
    
    def __init__(self, ai_settings, screen, ship):
        '''Utworzenie obiektu pocisku w aktualnym położeniu statku.'''
        super(Bullet, self).__init__()
        self.screen = screen
        
        # Utworzenie prostokąta pocisku w punkcie (0,0) a następnie zdefiniowa
        # nie dla niego odpowiedniego położenia.
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        
        # Położenie pocisku jest zdefiniowane za pomocą wartosci zmiennoprze-
        # cinkowej.
        self.y = float(self.rect.y)
        
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
        
    def update(self):
        '''Poruszanie pociskiem po ekranie.'''
        # Uaktualnienie położenia pocisku.
        self.y -= self.speed_factor
        self.rect.y = self.y  # Uaktualnienie położenia prostokąta pocisku.
        
    def draw_bullet(self):
        '''Wyswietlenie pocisku na ekranie.'''
        pygame.draw.rect(self.screen, self.color, self.rect)