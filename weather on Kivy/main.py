from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
import requests

api_url = "http://api.openweathermap.org/data/2.5/weather"


def weather_call(a):
    params = {
        'q': a,
        'appid': '75ee53bb395e2fe2c2644f810308ad58',
        'units': 'metric'
    }
    res = requests.get(api_url, params=params)
    data = res.json()
    x = data["main"]["temp"]
    return x


def weather_pict(a):
    params = {
        'q': a,
        'appid': '75ee53bb395e2fe2c2644f810308ad58',
        'units': 'metric'
    }
    res = requests.get(api_url, params=params)
    data = res.json()
    x = data["weather"]
    return x


class MainApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.instance = TextInput(
            multiline=False, readonly=True, halign="center", font_size=55
        )
        self.city = TextInput(
            multiline=False, halign="center", font_size=55
        )
        self.w_img = Image()

    def build(self):
        main_layout = BoxLayout(orientation="horizontal")
        left_layout = BoxLayout(orientation="vertical")
        right_layout = BoxLayout(orientation="vertical")
        left_layout.add_widget(self.instance)
        left_layout.add_widget(self.city)
        button = Button(text='Lets check temperature',
                        pos_hint={'center_x': .5, 'center_y': .5})
        button.bind(on_press=self.button_press)
        left_layout.add_widget(button)
        main_layout.add_widget(left_layout)
        right_layout.add_widget(self.w_img)
        main_layout.add_widget(right_layout)
        return main_layout

    def button_press(self, instance):
        x = self.city.text
        self.instance.text = str("Temp is " + str(weather_call(x)) + " C")
        y = weather_pict(x)
        print(y)
        for i in weather_pict(x):
            z = i['main']
            print(z)
            if z == 'Clouds':
                self.w_img.source = 'Clouds.jpg'
            elif z == 'Clear':
                self.w_img.source = 'Clear.jpg'
            elif z == 'Rain':
                self.w_img.source = 'Rain.jpg'


if __name__ == '__main__':
    MainApp().run()
