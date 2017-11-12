# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 23:01:42 2017

@author: Leszek
"""
import pygame
import pygame.display
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    '''Funkcja uruchamia grę.'''
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Inwazja obcych')
    # Utworzenie statku kosmicznego
    ship = Ship(screen)

    # Rozpoczęcie pętli głownej gry.
    while True:
        gf.check_events()
        gf.update_screen(ai_settings, screen, ship)


run_game()
