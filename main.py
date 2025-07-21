from kivy.app import App
from kivy.uix.label import Label

class PlanetfitApp(App):
    def build(self):
        return Label(text="Welcome to PlanetFit!")

if __name__ == '__main__':
    PlanetfitApp().run()
