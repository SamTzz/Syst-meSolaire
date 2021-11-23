import pygame
import random
from pygame import Vector2


class planete:
    def __init__(self):
        self.rayon = (random.randint(5,30))
        self.couleur = (random.randint(20, 215), random.randint(20, 215), random.randint(20, 215))
        self.position = Vector2(random.randint(15, 1585), random.randint(15, 875))
        self.masse = self.rayon * 2

    def draw(self, screen):
        pygame.draw.circle(screen, self.couleur, self.position, self.rayon)
