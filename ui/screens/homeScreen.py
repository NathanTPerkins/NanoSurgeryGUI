from kivy.uix.gridlayout import GridLayout
from ui.widgets.modeSwitch import ModeToggleSwtich
from ui.widgets.speedSlider import SpeedSlider
from ui.widgets.gearSwitch import GearPanel
from ui.widgets.armSlider import ArmSlider
from ui.widgets.armToggle import ExtendArmButton
from ui.widgets.clampButton import ClampArmButton
from ui.widgets.retractArm import RetractArmButton
from ui.widgets.releaseArm import ReleaseArmButton
from ui.widgets.movementPanel import MovementPanel
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.videoplayer import VideoPlayer

class SidePanel(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.add_widget(ModeToggleSwtich())
        self.add_widget(SpeedSlider())
        self.add_widget(ArmSlider())
        self.add_widget(ArmButtons())

class ArmButtons(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = self.rows = 2
        self.add_widget(ExtendArmButton())
        self.add_widget(RetractArmButton())
        self.add_widget(ClampArmButton())
        self.add_widget(ReleaseArmButton())

class MainScreen(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2
        self.rows = 2

        self.add_widget(VideoPlayer(source = "video.mkv", state='play',options={'eos':'loop'}, allow_fullscreen=False))
        self.add_widget(SidePanel())
        self.add_widget(GearPanel())
        self.add_widget(MovementPanel())
        