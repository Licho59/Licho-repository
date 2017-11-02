# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 21:53:44 2017

@author: Leszek
"""
### Gra w czołgi
from tank import Tank

tanks = {"a":Tank("Alice"), "b":Tank("Bob"), "c":Tank("Carol")}
alive_tanks = len(tanks)

while alive_tanks > 1:
    print()
    for tank_name in sorted(tanks.keys()):
        print(tanks[tank_name])
                   
    try:
        first_tank = tanks[input("Who fires? ").lower()]
        second_tank = tanks[input("Who at? ").lower()]
    except KeyError:
        print("No such tank!")
        continue
    
    if not first_tank.alive or not second_tank.alive:
        print("One of the tanks is dead!")
        continue
    
    print("*"*30)
    
    first_tank.fire_at(second_tank)
    if not second_tank.alive:
        alive_tanks -= 1
        
    print("*"*30)
    
for tank in tanks.values():
    if tank.alive:
        print(first_tank.name, "is the winner!")
        break
