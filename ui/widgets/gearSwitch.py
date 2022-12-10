from kivy.uix.togglebutton import ToggleButton
from kivy.uix.boxlayout import BoxLayout

class DriveGear(ToggleButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.group = "gears"
        self.text = "D"

    def on_press(self):
        if self.state == 'normal':
            self.state = 'down'



class ReverseGear(ToggleButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.group = "gears"
        self.text = "R"

    def on_press(self):
        if self.state == 'normal':
            self.state = 'down'


class HoverGear(ToggleButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.group = "gears"
        self.text = "H"
        self.state = 'down'

    def on_press(self):
        if self.state == 'normal':
            self.state = 'down'

class GearPanel(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'horizontal'
        self.add_widget(HoverGear())
        self.add_widget(DriveGear())
        self.add_widget(ReverseGear())