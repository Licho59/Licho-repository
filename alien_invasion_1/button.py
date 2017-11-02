# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 22:10:03 2017

@author: Leszek
"""

import pygame.font

class Button():
    '''Tworzy przycisk do uruchamiania gry.'''
    
    def __init__(self, ai_settings, screen, msg):
        '''Inicjalizacja atrybutow przycisku.'''
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        # Zdefiniowanie wymiarow i własciwowosci przycisku.
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        
        # Utworzenie prostokąta przycisku i wysrodkowanie go.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        
        # Komunikat wyswietlany przez przycisk trzeba przygotować jednokrotnie.
        self. prep_msg(msg)
        
    def prep_msg(self, msg):
        '''Umieszczenie komunikatu w wygenerowanym obrazie i wysrodkowanie
        tekstu na przycisku.'''
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        
    def draw_button(self):
        '''Wyswietlenie pustego przycisku, a następnie komunikatu na nim.'''
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)