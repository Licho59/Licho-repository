# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 23:22:23 2017

@author: Leszek
"""
class Settings():
    '''Klasa przeznaczona do  przechowywania wszystkich ustawień gry'''
    
    def __init__(self):
        '''Inicjalizacja ustawień gry.'''
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)