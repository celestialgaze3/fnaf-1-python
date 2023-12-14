from title_screen_gamestate import TitleScreenGameState
from office_gamestate import OfficeGameState
from display import Display

class Game:
    def __init__(self, screen):
        self.display = Display(self, screen)
        self.state = TitleScreenGameState(self, self.display)
        self.objects = {}
        
        self.ai_levels = {
            "Freddy": 20,
            "Bonnie": 20,
            "Chica": 20,
            "Foxy": 20
        }

        self.night = 7

        self.state.initialize()
    
    def switch_game_state(self, new_game_state):
        self.state.exit()
        self.state = new_game_state
        self.state.initialize()

    def start_new_game(self):
        self.switch_game_state(OfficeGameState(self, self.display))

    def add_object(self, id, game_object, layer=0):
        self.objects[id] = game_object
        self.display.add_object(id, layer)

    def remove_object(self, id):
        self.display.remove_object(id)
        if id in self.objects:
            del self.objects[id]