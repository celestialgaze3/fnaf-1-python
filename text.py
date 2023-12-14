import pygame
import os
from drawable import Drawable

class Text(Drawable):
    def __init__(self, state, rect: pygame.Rect, font: pygame.font.Font, string: str, color):
        Drawable.__init__(self, state, rect)
        self.font = font
        self.string = string
        self.color = color

        self.render_image()

    def render_image(self):
        self.image = self.font.render(self.string, True, self.color)

    def change_string(self, new_string):
        self.string = new_string
        self.render_image()

    def draw(self, screen):
        self.image = pygame.transform.scale(self.image, (self.rect[2], self.rect[3]))
        screen.blit(self.image, self.rect)