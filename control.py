from julia import Julia
from display import Screen
import pygame

class Control(object):
    def __init__(self, screen, julia):
        self.julia = julia
        self.screen = screen
        w, h = screen.screen.get_width(), screen.screen.get_height()
        self.output = pygame.display.set_mode((w, h+100))
        self.background = pygame.Surface((w,100))
        self.background.fill((199,199,199))
        self.output.blit(self.background.convert(), (0,h))
