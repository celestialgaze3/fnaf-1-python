import pygame
import os
from drawable import Drawable

class GameObject(Drawable, pygame.sprite.Sprite):
    def __init__(self, state, rect, texture_name):
        Drawable.__init__(self, state, rect)
        pygame.sprite.Sprite.__init__(self)
        self.texture_name = texture_name
        self.load_texture()

    def load_texture(self):
        self.image = pygame.image.load(os.path.join("assets", "textures", self.texture_name))

    def change_texture(self, new_texture_name):
        self.texture_name = new_texture_name
        self.load_texture()

    def draw(self, screen):
        if self.image == None:
            return
        
        #print("Rendering " + self.texture_name)
        self.image = pygame.transform.scale(self.image, (self.rect[2], self.rect[3]))
        screen.blit(self.image, self.rect)