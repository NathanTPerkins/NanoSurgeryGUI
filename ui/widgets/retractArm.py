from kivy.uix.togglebutton import ToggleButton

class RetractArmButton(ToggleButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = "Retract Arm"

    def on_release(self):
        self.state = 'normal'