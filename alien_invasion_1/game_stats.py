# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 19:36:22 2017

@author: Leszek
"""
class GameStats():
    '''Monitorowanie danych statystycznych w grze "Inwazja obcych".'''
    
    def __init__(self, ai_settings):
        '''Inicjalizacja danych statystycznych.'''
        self.ai_settings = ai_settings
        self.reset_stats()
        # Uruchomienie gry "Inwazja obcych" w stanie aktywnym.
        self.game_active = False
        
    def reset_stats(self):
        '''Inicjalizacja danych statystycznych, ktore mogą zmieniać się 
        w trakcie gry.'''
        self.ships_left = self.ai_settings.ship_limit