import core
import pygame
from pygame.math import Vector2
from soleil import soleil
from planete import planete



def setup():
    print("Setup START---------")

    core.fps = 60
    core.WINDOW_SIZE = [1600, 900]
    core.memory("soleil", soleil())
    core.memory("planete", planete())

    core.memory("direction", Vector2(0, 0))
    core.memory("G", 9.81)
    core.memory("Ft", 0)
    core.memory("Mab", 0)

    core.memory("planete", "planete_n°")
    core.memory("TableauDeplanete", [])
    for i in range(10):
        core.memory("TableauDeplanete").append(planete())



def run():
    core.cleanScreen()

    core.memory("soleil").draw(core.screen)
    #core.memory("planete").draw(core.screen)

    for i in core.memory("TableauDeplanete"):
        pygame.draw.circle(core.screen, i.couleur, i.position, i.rayon)






core.main(setup, run)
