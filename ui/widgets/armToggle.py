from kivy.uix.togglebutton import ToggleButton

class ExtendArmButton(ToggleButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = "Extend Arm"

    def on_release(self):
        self.state = 'normal'