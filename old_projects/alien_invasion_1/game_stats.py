class GameStats():
    '''Monitorowanie danych statystycznych w grze "Inwazja obcych".'''

    def __init__(self, ai_settings):
        '''Inicjalizacja danych statystycznych.'''
        self.ai_settings = ai_settings
        self.reset_stats()
        # Uruchomienie gry "Inwazja obcych" w stanie aktywnym.
        self.game_active = False
        # Najlepszy wynik nigdy nie powinien zostać wyzerowany
        self.high_score = 0
        self.level = 1

    def reset_stats(self):
        '''Inicjalizacja danych statystycznych, które mogą zmieniać się
        w trakcie gry.'''
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
