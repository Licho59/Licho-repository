# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 21:30:04 2017

@author: Leszek
"""
# Utworzenie klasy Tank
class Tank():
    """Modelowanie parametrow czołgu."""
    def __init__(self, name):
        """Inicjacja obiektu klasy Tank."""
        self.name = name
        self.alive = True
        self.ammo = 5
        self.armor = 60
        
    def __str__(self):
        """Zwraca łańcuch nazw opisujący dany obiekt."""
        if self.alive:
            return "%s (%i armor,%i shells)" % (self.name,self.armor,self.ammo)
        else:
            return "%s(DEAD)" % self.name
        
    def fire_at(self, enemy):
        """Wskazuje cel wroga."""
        if self.ammo >= 1:
            self.ammo -= 1
            print(self.name, "fires on", enemy.name)
            enemy.hit()
        else:
            print(self.name, "has no shells!")
    
    def hit(self):
        """Zwraca trafienie obiektu wroga."""
        self.armor -= 20
        print(self.name, "is hit!")
        if self.armor <= 0:
            self.explode()
            
    def explode(self):
        """Zwraca eksplozję obiektu wroga."""
        self.alive = False
        print(self.name, "explodes!")
        