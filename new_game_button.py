from button import Button

class NewGameButton(Button):

    def __init__(self, state, rect):
        Button.__init__(self, state, rect, "448.png", state.game.start_new_game)