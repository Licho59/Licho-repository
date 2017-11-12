import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats

from ship import Ship
import game_functions as gf


def run_game():
    '''Inicjalizacja gry i utworzenie ekranu'''
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Inwazja obcych")

    # Utworzenie egzemplarza przeznaczonego do przechowywania danych
    # statystycznych dotyczących gry.
    stats = GameStats(ai_settings)

    # Set the background color.
    bg_color = (230, 230, 230)
    
    # Utworzenie statku kosmicznego, grupy pocisków oraz grupy obcych.
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    # Utworzenie floty obcych.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Rozpoczęcie pętli głównej gry.
    while True:
        # Odswieżenie ekranu w trakcie każdej pętli.
        gf.check_events(ai_settings, screen, ship, bullets)
        
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
