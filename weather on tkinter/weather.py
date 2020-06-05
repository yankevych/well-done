import requests
from tkinter import *

root = Tk()
api_url = "http://api.openweathermap.org/data/2.5/weather"


def weather_call():
    params = {
        'q': c.get(),
        'appid': '11c0d3dc6093f7442898ee49d2430d20',
        'units': 'metric'
    }
    res = requests.get(api_url, params=params)
    data = res.json()
    v.set(data["main"]["temp"])
    v1.set(data["weather"])


v = StringVar()
v1 = StringVar()
c1 = Label(text='City please')
c1.pack()
c = Entry(width=20, justify=CENTER)
c.pack()
x = Label(justify=CENTER, textvariable=v)
x.pack()
x1 = Label(justify=CENTER, textvariable=v1)
x1.pack()
y = Button(width=3, height=2, text='Go', command=weather_call)
y.pack()

root.mainloop()
