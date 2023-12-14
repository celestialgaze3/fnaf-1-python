from button import Button

class CameraToggleButton(Button):

    def __init__(self, state, rect):
        Button.__init__(self, state, rect, "420.png", state.toggle_camera)