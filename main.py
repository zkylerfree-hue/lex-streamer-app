from kivy.app import App
from kivy.uix.label import Label

class LexOmegaApp(App):
    def build(self):
        return Label(text='Welcome to LEX-Ω!')

if __name__ == '__main__':
    LexOmegaApp().run()
