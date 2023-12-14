from game_object import GameObject
from camera_map import CameraMap
import pygame
import os
import random

OVERLAY = "11.png"

class Camera(GameObject):

    def __init__(self, state, rect, room):
        GameObject.__init__(self, state, rect, OVERLAY)
        self.display = GameObject(state, pygame.Rect(0, 0, 1920, 1080), room.get_texture())
        self.map = CameraMap(state, pygame.Rect(1250, 440, 640, 640), room)
        self.room = room
        self.open = False

    def toggle_camera(self):
        if self.open:
            self.hide_camera()
        else:
            self.show_camera()

    def show_camera(self):
        self.state.add_object("camera_map", self.map, 3)
        self.state.add_object("camera_view", self.display, 2)
        self.state.add_object("camera_outline", self, 4)
        self.state.remove_object("left_office_controls")
        self.state.remove_object("right_office_controls")
        self.map.show_camera()
        self.change_camera(self.room)
        self.open = True

    def hide_camera(self):
        self.state.remove_object("camera_outline")
        self.state.remove_object("camera_view")
        self.state.remove_object("camera_map")
        self.map.hide_camera()
        self.state.add_object("left_office_controls", self.state.office.left_office_controls, 1)
        self.state.add_object("right_office_controls", self.state.office.right_office_controls, 1)
        self.state.animatronics["Foxy"].stall_time = random.randint(1, 18)
        self.open = False

    def update_camera(self):
        self.change_camera(self.room, update=True)

    def change_camera(self, room, update=False):
        self.room = room
        self.display.change_texture(room.get_texture())
        if room.id == "2A" and "Foxy" in room.animatronics and not update:
            self.state.animatronics["Foxy"].seen_in_west_hall()

        # Stall Freddy in rooms where we look at the cameras
        if "Freddy" in room.animatronics and room.id != "1A":
            self.state.animatronics["Freddy"].stall_time = 5