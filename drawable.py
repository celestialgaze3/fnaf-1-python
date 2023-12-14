from game_state_member import GameStateMember

class Drawable:
    def __init__(self, state, rect):
        GameStateMember.__init__(self, state)
        self.rect = rect

    def draw():
        print("Unimplemented draw call")