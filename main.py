from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import threading
import time
import requests
import io
from PIL import Image
import subprocess
import os

SERVER_URL = "https://3cd2e6772dd851.lhr.life/upload"

class StreamApp(App):
    def build(self):
        self.streaming = False
        layout = BoxLayout(orientation='vertical', padding=50, spacing=30)
        
        self.label = Label(text="حالة البث: متوقف", font_size=24)
        layout.add_widget(self.label)
        
        self.start_btn = Button(text="تشغيل البث", font_size=22, background_color=(0, 1, 0, 1))
        self.start_btn.bind(on_press=self.start_stream)
        layout.add_widget(self.start_btn)
        
        self.stop_btn = Button(text="إيقاف البث", font_size=22, background_color=(1, 0, 0, 1))
        self.stop_btn.bind(on_press=self.stop_stream)
        layout.add_widget(self.stop_btn)
        
        return layout

    def start_stream(self, instance):
        if not self.streaming:
            self.streaming = True
            self.label.text = "حالة البث: يعمل الآن..."
            self.thread = threading.Thread(target=self.stream_loop)
            self.thread.daemon = True
            self.thread.start()

    def stop_stream(self, instance):
        self.streaming = False
        self.label.text = "حالة البث: متوقف"

    def stream_loop(self):
        while self.streaming:
            try:
                subprocess.run(["screencap", "-p", "screen_temp.png"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                if os.path.exists("screen_temp.png") and os.path.getsize("screen_temp.png") > 0:
                    img = Image.open("screen_temp.png")
                    img = img.resize((480, 854))
                    img_byte_arr = io.BytesIO()
                    img.save(img_byte_arr, format='JPEG', quality=70)
                    img_byte_arr = img_byte_arr.getvalue()
                    requests.post(SERVER_URL, files={"frame": img_byte_arr})
                time.sleep(0.1)
            except Exception as e:
                time.sleep(1)

if __name__ == '__main__':
    StreamApp().run()
