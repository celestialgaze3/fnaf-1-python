from game_object import GameObject

LEFT_DOOR_OPEN = "88.png"
LEFT_DOOR_CLOSED = "102.png"
RIGHT_DOOR_OPEN = "104.png"
RIGHT_DOOR_CLOSED = "118.png"

class OfficeDoors(GameObject):

    def __init__(self, state, rect, left):
        GameObject.__init__(self, state, rect, LEFT_DOOR_OPEN)
        self.left = left
        self.set_texture_open()
    
    def set_texture_open(self):
        self.change_texture(LEFT_DOOR_OPEN if self.left else RIGHT_DOOR_OPEN)

    def set_texture_closed(self):
        self.change_texture(LEFT_DOOR_CLOSED if self.left else RIGHT_DOOR_CLOSED)