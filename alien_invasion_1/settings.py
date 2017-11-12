# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 22:56:26 2017

@author: Ja
"""


class Settings():
    '''Klasa przeznaczona do przechowywania wszystkich ustawień gry.'''

    def __init__(self):
        '''Inicjalizacja ustawień gry.'''
        # Ustawienia ekranu.
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # Ustawienia dotyczące statku.
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # Ustawienia dotyczące pocisku
        self.bullet_speed_factor = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # Ustawienia dotyczące obcego
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 30
        self.fleet_direction = 1  # wartosc fleet_direction wynosząca 1 oznacza
        # prawo, natomiast - 1 oznacza lewo
