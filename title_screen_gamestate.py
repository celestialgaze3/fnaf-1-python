import pygame
from gamestate import GameState
from game_object import GameObject
from new_game_button import NewGameButton

class TitleScreenGameState(GameState):

    def initialize(self):
        GameState.initialize(self)
        self.add_object("background", GameObject(self, pygame.Rect(0, 0, 1920, 1080), "431.png"))
        self.add_object("new_game", NewGameButton(self, pygame.Rect(100, 100, 400, 75)))

    def exit(self):
        GameState.exit(self)
        