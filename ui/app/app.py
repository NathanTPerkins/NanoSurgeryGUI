from kivy.app import App
from ui.screens.homeScreen import MainScreen

class NanoSurgeryApp(App):
    def __init__(self, **kwargs):
        super(NanoSurgeryApp, self).__init__(**kwargs)

        self.title = "Nano-Surgery"

    def build(self):
        
        return MainScreen()
    
    def on_start(self):
        return super().on_start()

    def on_stop(self):
        return super().on_stop()