from kivy.uix.slider import Slider
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class SpeedSliderBar(Slider):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'horizontal'
        self.max = 10
        self.min = 0
        self.value = 5
        self.step = 1
        self.value_track = True

class SpeedSliderLabel(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = "Speed\n5.0"

    def OnSliderValueChange(self, instance, value):
        self.text = "Speed\n" + str(value)

class SpeedSlider(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"

        slider = SpeedSliderBar()
        label = SpeedSliderLabel()
        slider.bind(value = label.OnSliderValueChange)

        self.add_widget(label)
        self.add_widget(slider)