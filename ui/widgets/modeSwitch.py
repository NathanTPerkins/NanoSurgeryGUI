from kivy.uix.switch import Switch
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.graphics import Canvas

class AutoPilotLabel(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = "AutoPilot"
        self.color = [0.3,0.3,0.3,1]

class AutoPilotSwitch(Switch):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class ModeToggleSwtich(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.add_widget(AutoPilotLabel())
        self.add_widget(AutoPilotSwitch())


        
