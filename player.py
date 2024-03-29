import pygame
from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)

        self.image = pygame.image.load("images/Player.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
