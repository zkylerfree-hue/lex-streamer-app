from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class LexStreamerApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        
        self.label = Label(text="Lex Streamer Control", font_size=24)
        layout.add_widget(self.label)
        
        self.url = TextInput(text="http://server-ip:port", multiline=False)
        layout.add_widget(self.url)
        
        self.btn = Button(text="OFF", font_size=22)
        self.btn.bind(on_press=self.click)
        layout.add_widget(self.btn)
        
        return layout

    def click(self, instance):
        if self.btn.text == "OFF":
            self.btn.text = "ON"
            self.label.text = "Streaming Active"
        else:
            self.btn.text = "OFF"
            self.label.text = "Stopped"

if __name__ == '__main__':
    LexStreamerApp().run()
