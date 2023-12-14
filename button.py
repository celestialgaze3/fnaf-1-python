from game_object import GameObject

class Button(GameObject):
    def __init__(self, state, rect, texture_name, execute):
        GameObject.__init__(self, state, rect, texture_name)
        self.execute = execute
    
    def on_click(self, click_position):
        self.execute()