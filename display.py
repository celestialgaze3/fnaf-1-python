from game_object import GameObject

class Display:

    def __init__(self, game, screen):
        self.layers = {}
        self.game = game
        self.screen = screen

    def create_layer(self, layer_number):
        self.layers[layer_number] = []

    def set_layer(self, id, layer):
        self.remove_object(id)
        self.add_object(id, layer)

    def add_object(self, id, layer):
        if layer not in self.layers:
            self.create_layer(layer)
        self.layers[layer].append(id)

    def remove_object(self, id):
        for layer in self.layers:
            if id in self.layers[layer]:
                self.layers[layer].remove(id)
