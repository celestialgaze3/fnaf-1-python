from button import Button
from game_object import GameObject
import pygame
import os

SELECTED_BUTTON = "166.png"
UNSELECTED_BUTTON = "167.png"
UNSELECTED_BUTTON = "167.png"

button_labels = {
    "1A": "170.png",
    "1B": "171.png",
    "1C": "177.png",
    "2A": "172.png",
    "2B": "165.png",
    "3": "168.png",
    "4A": "169.png",
    "4B": "173.png",
    "5": "174.png",
    "6": "175.png",
    "7": "176.png"
}

class CameraSelectRoomButton(Button):

    def __init__(self, state, rect, room_id: str, execute):
        Button.__init__(self, state, rect, UNSELECTED_BUTTON, execute)
        self.room_id = room_id
        self.audio_change_camera = pygame.mixer.Sound(os.path.join("assets", "audio", "blip3.wav"))
        self.label = GameObject(state, pygame.Rect(rect[0] + rect[2] // 10, rect[1] + rect[3] // 10, rect[2] // 2, rect[3] // 5 * 3), button_labels[room_id])
    
    def update_texture(self):
        if self.state.camera.room.id == self.room_id:
            self.change_texture(SELECTED_BUTTON)
        else:
            self.change_texture(UNSELECTED_BUTTON)

    def on_click(self, click_position):
        self.execute(self.state.rooms[self.room_id])
        self.update_texture()
        pygame.mixer.Sound.play(self.audio_change_camera)

    def show_camera(self):
        self.state.add_object(f"camera_button_label_{self.room_id}", self.label, 3)

    def hide_camera(self):
        self.state.remove_object(f"camera_button_label_{self.room_id}")