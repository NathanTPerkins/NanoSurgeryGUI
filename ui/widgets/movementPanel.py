from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget

class UpButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = 'Up'

class DownButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = 'Down'

class LeftButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = 'Left'

class RightButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = 'Right'

class BreaksButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = 'Break'

class PushButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = 'Push'

class MovementPanel(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 3
        self.rows = 3
        self.add_widget(PushButton())
        self.add_widget(UpButton())
        self.add_widget(Widget())
        self.add_widget(LeftButton())
        self.add_widget(BreaksButton())
        self.add_widget(RightButton())
        self.add_widget(Widget())
        self.add_widget(DownButton())
        self.add_widget(Widget())

        self.padding = [10,10,10,10]
        self.spacing = [10,10]