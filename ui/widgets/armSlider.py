from kivy.uix.slider import Slider
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class ArmSliderBar(Slider):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'horizontal'
        self.max = 10
        self.min = 0
        self.value = 5
        self.step = 1
        self.value_track = True

class ArmSliderLabel(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = "Arm Length\n5.0"

    def OnSliderValueChange(self, instance, value):
        self.text = "Arm Length\n" + str(value)

class ArmSlider(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"

        slider = ArmSliderBar()
        label = ArmSliderLabel()
        slider.bind(value = label.OnSliderValueChange)

        self.add_widget(label)
        self.add_widget(slider)