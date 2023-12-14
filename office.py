import pygame
from game_object import GameObject
from office_controls import OfficeControls
from office_doors import OfficeDoors
import os

DORMANT = "39.png"
LEFT_LIGHT_ON = "58.png"
LEFT_LIGHT_BONNIE = "225.png"
RIGHT_LIGHT_ON = "127.png"
RIGHT_LIGHT_CHICA = "227.png"

class Office(GameObject):

    def __init__(self, state, rect):
        GameObject.__init__(self, state, rect, DORMANT)
        self.audio_door = pygame.mixer.Sound(os.path.join("assets", "audio", "door.mp3"))
        self.audio_lights = pygame.mixer.Sound(os.path.join("assets", "audio", "BallastHumMedium2.wav"))

        self.left_office_controls = OfficeControls(state, pygame.Rect(-20, 400, 117, 350), self, True)
        self.right_office_controls = OfficeControls(state, pygame.Rect(1800, 400, 117, 350), self, False)

        state.add_object("left_office_controls", self.left_office_controls, 1)
        state.add_object("right_office_controls", self.right_office_controls, 1)

        self.left_door = OfficeDoors(state, pygame.Rect(100, 0, 300, 1080), True)
        self.right_door = OfficeDoors(state, pygame.Rect(1520, 0, 300, 1080), False)
        
        state.add_object("left_door", self.left_door, 1)
        state.add_object("right_door", self.right_door, 1)

        self.left_light_on = False
        self.right_light_on = False
        self.left_door_closed = False
        self.right_door_closed = False
    
    def activate_left_light(self):
        self.left_light_on = True
        self.right_light_on = False
        self.change_texture(LEFT_LIGHT_BONNIE if "Bonnie" in self.state.rooms["OL"].animatronics else LEFT_LIGHT_ON)
        self.update_door_controls()
        pygame.mixer.Sound.play(self.audio_lights)
        
    def activate_right_light(self):
        self.left_light_on = False
        self.right_light_on = True
        self.change_texture(RIGHT_LIGHT_CHICA if "Chica" in self.state.rooms["OR"].animatronics else RIGHT_LIGHT_ON)
        self.update_door_controls()
        pygame.mixer.Sound.play(self.audio_lights)

    def activate_left_door(self):
        self.left_door_closed = True
        self.left_door.set_texture_closed()
        self.update_door_controls()
        pygame.mixer.Sound.play(self.audio_door)
        
    def activate_right_door(self):
        self.right_door_closed = True
        self.right_door.set_texture_closed()
        self.update_door_controls()
        pygame.mixer.Sound.play(self.audio_door)

    def deactivate_left_door(self):
        self.left_door_closed = False
        self.left_door.set_texture_open()
        self.update_door_controls()
        pygame.mixer.Sound.play(self.audio_door)
        
    def deactivate_right_door(self):
        self.right_door_closed = False
        self.right_door.set_texture_open()
        self.update_door_controls()
        pygame.mixer.Sound.play(self.audio_door)

    def deactivate_lights(self):
        self.left_light_on = False
        self.right_light_on = False
        self.change_texture(DORMANT)
        self.update_door_controls()
        pygame.mixer.Sound.stop(self.audio_lights)

    def update_door_controls(self):
        if self.left_light_on and self.left_door_closed:
            self.left_office_controls.set_texture_both()
        elif self.left_light_on:
            self.left_office_controls.set_texture_light()
        elif self.left_door_closed:
            self.left_office_controls.set_texture_door()
        else:
            self.left_office_controls.set_texture_inactive()

        if self.right_light_on and self.right_door_closed:
            self.right_office_controls.set_texture_both()
        elif self.right_light_on:
            self.right_office_controls.set_texture_light()
        elif self.right_door_closed:
            self.right_office_controls.set_texture_door()
        else:
            self.right_office_controls.set_texture_inactive()

        