from game_object import GameObject
from button import Button

LEFT_CONTROLS_INACTIVE = "122.png"
LEFT_CONTROLS_DOOR = "124.png"
LEFT_CONTROLS_LIGHT = "125.png"
LEFT_CONTROLS_BOTH = "130.png"

RIGHT_CONTROLS_INACTIVE = "134.png"
RIGHT_CONTROLS_DOOR = "135.png"
RIGHT_CONTROLS_LIGHT = "131.png"
RIGHT_CONTROLS_BOTH = "47.png"

class OfficeControls(Button):

    def __init__(self, state, rect, office, left):
        GameObject.__init__(self, state, rect, LEFT_CONTROLS_INACTIVE)
        self.office = office
        self.left = left
        self.set_texture_inactive()
    
    def set_texture_inactive(self):
        self.change_texture(LEFT_CONTROLS_INACTIVE if self.left else RIGHT_CONTROLS_INACTIVE)

    def set_texture_door(self):
        self.change_texture(LEFT_CONTROLS_DOOR if self.left else RIGHT_CONTROLS_DOOR)

    def set_texture_light(self):
        self.change_texture(LEFT_CONTROLS_LIGHT if self.left else RIGHT_CONTROLS_LIGHT)

    def set_texture_both(self):
        self.change_texture(LEFT_CONTROLS_BOTH if self.left else RIGHT_CONTROLS_BOTH)

    def is_door_press(self, click_position) -> bool:
        return click_position[1] < self.rect[1] + self.rect[3] // 2
    
    def is_light_press(self, click_position) -> bool:
        return click_position[1] >= self.rect[1] + self.rect[3] // 2
    
    def on_click(self, click_position):
        if self.is_light_press(click_position):
            if self.left:
                if self.office.left_light_on:
                    self.office.deactivate_lights()
                else:
                    self.office.activate_left_light()
            else:
                if self.office.right_light_on:
                    self.office.deactivate_lights()
                else:
                    self.office.activate_right_light()
        elif self.is_door_press(click_position):
            if self.left:
                if self.office.left_door_closed:
                    self.office.deactivate_left_door()
                else:
                    self.office.activate_left_door()
            else:
                if self.office.right_door_closed:
                    self.office.deactivate_right_door()
                else:
                    self.office.activate_right_door()

