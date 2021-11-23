import pygame
from pygame import Vector2


class soleil:
    def __init__(self):
        self.rayon = 70
        self.couleur = (255, 255, 0)
        self.position = Vector2(800, 450)
        self.masse = self.rayon*2

    def draw(self, screen):
        pygame.draw.circle(screen, self.couleur, self.position, self.rayon)
