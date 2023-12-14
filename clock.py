from game_object import GameObject
from game_state_member import GameStateMember
import pygame

ONE = "252.png"
TWO = "253.png"
THREE = "254.png"
FOUR = "255.png"
FIVE = "256.png"
SIX = "257.png"
AM = "352.png"

class Clock(GameStateMember):

    def __init__(self, state, rect, hour):
        GameStateMember.__init__(self, state)
        self.rect = rect
        self.clock_digit_left_one = GameObject(state, pygame.Rect(rect[0], rect[1], 30, 50), ONE)
        self.clock_digit_right_one = GameObject(state, pygame.Rect(rect[0] + 30, rect[1], 30, 50), ONE)
        self.clock_digit_right_two = GameObject(state, pygame.Rect(rect[0] + 30, rect[1], 30, 50), TWO)
        self.clock_digit_right_three = GameObject(state, pygame.Rect(rect[0] + 30, rect[1], 30, 50), THREE)
        self.clock_digit_right_four = GameObject(state, pygame.Rect(rect[0] + 30, rect[1], 30, 50), FOUR)
        self.clock_digit_right_five = GameObject(state, pygame.Rect(rect[0] + 30, rect[1], 30, 50), FIVE)
        self.clock_digit_right_six = GameObject(state, pygame.Rect(rect[0] + 30, rect[1], 30, 50), SIX)
        self.clock_am = GameObject(state, pygame.Rect(rect[0] + 75, rect[1], 60, 50), AM)

        self.hour = hour
        self.update_texture()
    
    def set_hour(self, hour):
        self.hour = hour
        self.update_texture()

    def update_texture(self):
        self.clear_textures()
        if self.hour == 0:
            self.state.add_object("clock_digit_left_one", self.clock_digit_left_one, 5)
            self.state.add_object("clock_digit_right_two", self.clock_digit_right_two, 5)
        elif self.hour == 1:
            self.state.add_object("clock_digit_right_one", self.clock_digit_right_one, 5)
        elif self.hour == 2:
            self.state.add_object("clock_digit_right_two", self.clock_digit_right_two, 5)
        elif self.hour == 3:
            self.state.add_object("clock_digit_right_three", self.clock_digit_right_three, 5)
        elif self.hour == 4:
            self.state.add_object("clock_digit_right_four", self.clock_digit_right_four, 5)
        elif self.hour == 5:
            self.state.add_object("clock_digit_right_five", self.clock_digit_right_five, 5)
        elif self.hour == 6:
            self.state.add_object("clock_digit_right_six", self.clock_digit_right_six, 5)
        self.state.add_object("clock_am", self.clock_am, 5)

    def clear_textures(self):
        self.state.remove_object("clock_digit_left_one")
        self.state.remove_object("clock_digit_right_one")
        self.state.remove_object("clock_digit_right_two")
        self.state.remove_object("clock_digit_right_three")
        self.state.remove_object("clock_digit_right_four")
        self.state.remove_object("clock_digit_right_five")
        self.state.remove_object("clock_digit_right_six")
        self.state.remove_object("clock_am")