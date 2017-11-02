# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 15:11:41 2017

@author: Leszek
"""

import pygame, sys

screen = pygame.display.set_mode((800, 600))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()