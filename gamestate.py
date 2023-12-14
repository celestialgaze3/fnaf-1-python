class GameState:
    def __init__(self, game, display):
        self.objects = []
        self.game = game # Reference to the main game object
        self.display = display # Reference to the main window's display

    def initialize(self):
        pass # Implemented in subclass

    def exit(self):
        self.clear_all_objects()

    def add_object(self, id, game_object, layer=0):
        self.game.add_object(id, game_object, layer)
        self.objects.append(id)
    
    def remove_object(self, id):
        self.game.remove_object(id)
        if id in self.objects:
            self.objects.remove(id)

    def clear_all_objects(self):
        for id in self.objects:
            self.game.remove_object(id)
        self.objects.clear()
    