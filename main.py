import requests
from tkinter import*
root=Tk()
root.geometry("400x400")
root.title("Weather")
def weather1():
    x=enter.get()
    api = 'ce1c1ddf03c62a1a15c3b1fda4ed5032'
    param = {"q": x, 'appid': api, "units": "metric"}
    resp = requests.get('https://api.openweathermap.org/data/2.5/weather', params=param)
    resp2 = resp.json()
    print(resp.json())
    label['text']=f"В місті {resp2['name']}\n температура повітря {int(resp2['main']['temp'])}"
    print(resp2["name"])
enter = Entry(root, width=20)
enter.pack()
label = Label(root, text="Weather forecast")
label.pack()
button = Button(root, text="Show weather", command=weather1)
button.pack()
root.mainloop()