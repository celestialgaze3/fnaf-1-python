from game_object import GameObject
from camera_select_room_button import CameraSelectRoomButton
import pygame

class CameraMap(GameObject):

    def __init__(self, state, rect, selected_room_id):
        GameObject.__init__(self, state, rect, "145.png")
        self.selected_room_id = selected_room_id

        left = rect[0]
        top = rect[1]
        width = rect[2]
        height = rect[3]

        self.buttons = {
            "1A": CameraSelectRoomButton(state, pygame.Rect(left + width // 4, top + height // 15, 75, 50), "1A", self.select_room),
            "1B": CameraSelectRoomButton(state, pygame.Rect(left + width // 9 * 2, top + height // 5, 75, 50), "1B", self.select_room),
            "1C": CameraSelectRoomButton(state, pygame.Rect(left + width // 6, top + height // 5 * 2, 75, 50), "1C", self.select_room),
            "2A": CameraSelectRoomButton(state, pygame.Rect(left + width // 32 * 9, top + height // 16 * 11, 75, 50), "2A", self.select_room),
            "2B": CameraSelectRoomButton(state, pygame.Rect(left + width // 32 * 9, top + height // 32 * 25, 75, 50), "2B", self.select_room),
            "3": CameraSelectRoomButton(state, pygame.Rect(left + width // 10, top + height // 8 * 5, 75, 50), "3", self.select_room),
            "4A": CameraSelectRoomButton(state, pygame.Rect(left + width // 2, top + height // 16 * 11, 75, 50), "4A", self.select_room),
            "4B": CameraSelectRoomButton(state, pygame.Rect(left + width // 2, top + height // 32 * 25, 75, 50), "4B", self.select_room),
            "5": CameraSelectRoomButton(state, pygame.Rect(left - width // 32, top + height // 4, 75, 50), "5", self.select_room),
            "6": CameraSelectRoomButton(state, pygame.Rect(left + width // 16 * 13, top + height // 32 * 19, 75, 50), "6", self.select_room),
            "7": CameraSelectRoomButton(state, pygame.Rect(left + width // 8 * 6, top + height // 4, 75, 50), "7", self.select_room)
        }
    
    def select_room(self, room):
        self.state.camera.change_camera(room)
        for id in self.buttons:
            self.buttons[id].update_texture()

    def show_camera(self):
        for id in self.buttons:
            self.state.add_object(f"camera_button_{id}", self.buttons[id], 3)
            self.buttons[id].show_camera()

    def hide_camera(self):
        for id in self.buttons:
            self.state.remove_object(f"camera_button_{id}")
            self.buttons[id].hide_camera()