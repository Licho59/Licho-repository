# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 20:22:54 2017

@author: Leszek
"""
# Zadanie 13.1 Gwiazdy
import pygame
from pygame.sprite import Group
from stars_settings import Settings
from star import Star
#import game_functions as gf

def get_number_stars_x(stars_settings, star_width):
    '''Ustalenie liczby gwiazd, które zmieszczą się w rzędzie.'''
    available_space_x = stars_settings.screen_width - 2 * star_width
    number_stars_x = int(available_space_x / (2 * star_width))
    return number_stars_x

def get_number_rows(stars_settings, star_height):
    '''Ustalenie, ile rzędów obcych zmiesci się na ekranie.'''
    available_space_y = (stars_settings.screen_height - (3 * star_height))
    number_rows = int(available_space_y / (2 * star_height))
    return number_rows

def create_star(stars_settings, screen, stars, star_number, row_number):
    '''Utworzenie gwiazdy i umieszczenie jej w rzędzie.'''
    star = Star(stars_settings, screen)
    star_width = star.rect.width
    star.x = star_width + 2 * star_width * star_number
    star.rect.x = star.x
    star.rect.y = star.rect.height + 2 * star.rect.height * row_number
    stars.add(star)
            
def create_fleet(stars_settings, screen, stars):
    '''Utworzenie pełnej floty gwiazd.'''
    # Utworz. gwiazdy i ustalenie liczby gwiazd, które zmieszczą się w rzędzie.
    star = Star(stars_settings, screen)
    number_stars_x = get_number_stars_x(stars_settings, star.rect.width)
    number_rows = get_number_rows(stars_settings, star.rect.height)
      
    # Utworzenie floty gwiazd.
    for row_number in range(number_rows):
        for star_number in range(number_stars_x):
            create_star(stars_settings, screen, stars, star_number, row_number)

def update_screen(stars_settings, screen, stars):
    '''Uaktualnienie obrazów na ekranie i przejscie do nowego ekranu.'''
    # Odswieżenie ekranu w trakcie każdej iteracji pętli.
    screen.fill(stars_settings.bg_color)
    stars.draw(screen)            
#==============================================================================
# def check_fleet_edges(stars_settings, stars):
#     '''Odpowiednia reakcja, gdy gwiazda dotrze do krawędzi ekranu.'''
#     for star in stars.sprites():
#         if star.check_fleet_edges():
#             change_fleet_direction(stars_settings, stars)
#             break
#         
# def change_fleet_direction(stars_settings, stars):
#     '''Przesunięcie całej floty w dół i zmiana kierunku, w którym się ona
#     porusza.'''
#     for star in stars.sprites():
#         star.rect.y += stars_settings.fleet_drop_speed
#     stars_settings.fleet_direction *= -1
#==============================================================================

#==============================================================================
# def update_stars(stars_settings, stars):
#     '''Sprawdzenie, czy flota znajduje się przy krawędzi ekranu, a następnie
#     uaktualnienie położenia wszystkich obcych we flocie.'''
#     #check_fleet_edges(stars_settings, stars)
#     stars.update()
#==============================================================================

def run_game():
    '''Inicjalizacja gry i utworzenie ekranu'''
    pygame.init()
    stars_settings = Settings()
    screen = pygame.display.set_mode((stars_settings.screen_width,
                                      stars_settings.screen_height))
    pygame.display.set_caption("Siatka gwiazd")    
    
    # Utworzenie statku kosmicznego, grupy pocisków oraz grupy obcych.
#==============================================================================
#     ship = Ship(ai_settings, screen)
#     bullets = Group()
#==============================================================================
    stars = Group()
    # Utworzenie siatki gwiadz.
    create_fleet(stars_settings, screen, stars)
    
    # Rozpoczęcie pętli głównej gry.
    while True: 
        # Odswieżenie ekranu w trakcie każdej pętli.
#==============================================================================
#        gf.check_events(ai_settings, screen, ship, bullets)
#        ship.update()
#        gf.update_bullets(bullets)
#==============================================================================
       # update_stars(stars_settings, stars)
        update_screen(stars_settings, screen, stars)
                     
run_game()