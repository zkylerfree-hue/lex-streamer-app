from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class LexStreamerApp(App):
    def build(self):
        self.title = "Lex Streamer App"
        
        # تخطيط الشاشة عمودياً
        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        
        # عنوان التطبيق
        self.header_label = Label(
            text="Lex Streamer Control", 
            font_size=24, 
            size_hint_y=None, 
            height=50
        )
        layout.add_widget(self.header_label)
        
        # خانة إدخال رابط السيرفر
        self.url_input = TextInput(
            text="http://your-server-ip:port", 
            multiline=False, 
            size_hint_y=None, 
            height=50
        )
        layout.add_widget(self.url_input)
        
        # زر التشغيل والإيقاف (ON / OFF)
        self.toggle_btn = Button(
            text="OFF", 
            background_color=(0.8, 0.2, 0.2, 1),
            font_size=22,
            size_hint_y=None,
            height=60
        )
        self.toggle_btn.bind(on_press=self.toggle_stream)
        layout.add_widget(self.toggle_btn)
        
        return layout

    def toggle_stream(self, instance):
        if self.toggle_btn.text == "OFF":
            self.toggle_btn.text = "ON"
            self.toggle_btn.background_color = (0.2, 0.8, 0.2, 1)
            self.header_label.text = "Status: Streaming Active"
        else:
            self.toggle_btn.text = "OFF"
            self.toggle_btn.background_color = (0.8, 0.2, 0.2, 1)
            self.header_label.text = "Status: Stopped"

if __name__ == '__main__':
    LexStreamerApp().run()
