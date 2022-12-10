from kivy.uix.togglebutton import ToggleButton

class ReleaseArmButton(ToggleButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = "Release Arm"

    def on_release(self):
        self.state = 'normal'