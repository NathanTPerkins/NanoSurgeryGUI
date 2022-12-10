from kivy.uix.togglebutton import ToggleButton

class ClampArmButton(ToggleButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = "Clamp Arm"

    def on_release(self):
        self.state = 'normal'
