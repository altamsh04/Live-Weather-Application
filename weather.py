from tkinter import *
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup as bs

root = Tk()
root.geometry("430x480")
root.config(background='#1C2833')
root.title("Weather Application")

photoicon = PhotoImage(file="partly_cloudy.png")
root.iconphoto(False, photoicon)


def get_weather_info(city):
    try:
        url = f"https://www.google.com/search?q={city.replace(' ', '')}+weather"
        session = requests.Session()
        session.headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/91.0.864.59"
        html = session.get(url)
        soup = bs(html.text, "html.parser")

        wname = soup.find('span', attrs={'id': 'wob_dc'}).text
        temp = soup.find('span', attrs={'id': 'wob_tm'}).text
        time = soup.find('div', attrs={'id': 'wob_dts'}).text

        pp = soup.find('span', attrs={'id': 'wob_pp'}).text
        hm = soup.find('span', attrs={'id': 'wob_hm'}).text
        ws = soup.find('span', attrs={'id': 'wob_ws'}).text
        namec = soup.find('span', attrs={'class': 'BBwThe'})
        loc = namec.string

        timeurl = f"https://www.google.com/search?q=current+time+in+{city.replace(' ', '')}"
        timesession = requests.Session()
        timesession.headers[
            'User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/91.0.864.59"
        timehtml = timesession.get(timeurl)
        timesoup = bs(timehtml.text, "html.parser")
        citytime = timesoup.find('div', attrs={'class': 'gsrt vk_bk FzvWSb YwPhnf'})
        realtime = citytime.string

        return wname, temp, time, pp, hm, ws, loc, realtime

    except Exception as e:
        print(f"Error: {e}")
        return None


def update_labels(city):
    result = get_weather_info(city)
    if result:
        wname, temp, time, pp, hm, ws, loc, realtime = result

        t1.config(text=wname)
        t2.config(text="Current time " + realtime)
        t3.config(text=time)
        t4.config(text="Precipitation: " + pp)
        t5.config(text="Humidity: " + hm)
        t6.config(text="Wind: " + ws)
        t0.config(text=loc)
        tempt.config(text=temp + "°C")

        imgstr = wname.lower()
        img_path = image_mapping.get(imgstr, 'default.png')
        img.config(file=img_path)


def find_weather():
    city = text.get()
    if len(city) != 0:
        update_labels(city)
    else:
        messagebox.showinfo(title='Warning message', message='Please enter a city name.')


title = Label(text="Weather Application", font='Consolas 15 bold', fg='#45B4FF', bg='#1C2833')
title.place(x=80, y=10)

label = Label(text="City Name:", font='Consolas 10 bold', fg='#45B4FF', bg='#1C2833')
label.place(x=15, y=80)

text = Entry(font='Consolas 9 bold', fg='#1C2833')
text.place(x=130, y=80)

btn = Button(text="Find Weather", font='Consolas 9 bold', fg='black', bg='#45B4FF', command=find_weather)
btn.place(x=310, y=75)

img = PhotoImage()
imgt = Label(root, image=img, bg='#1C2833')
imgt.place(x=130, y=140)

tempt = Label(root, font='Consolas 22 bold', fg='#45B4FF', bg='#1C2833')
tempt.place(x=220, y=150)

t0 = Label(root, font='Consolas 10 bold', fg='#45B4FF', bg='#1C2833')
t0.place(x=30, y=250)

t1 = Label(root, font='Consolas 10 bold', fg='#45B4FF', bg='#1C2833')
t1.place(x=30, y=280)

t2 = Label(root, font='Consolas 10 bold', fg='#45B4FF', bg='#1C2833')
t2.place(x=30, y=310)

t3 = Label(root, font='Consolas 10 bold', fg='#45B4FF', bg='#1C2833')
t3.place(x=30, y=340)

t4 = Label(root, font='Consolas 10 bold', fg='#45B4FF', bg='#1C2833')
t4.place(x=30, y=370)

t5 = Label(root, font='Consolas 10 bold', fg='#45B4FF', bg='#1C2833')
t5.place(x=30, y=400)

t6 = Label(root, font='Consolas 10 bold', fg='#45B4FF', bg='#1C2833')
t6.place(x=30, y=430)

image_mapping = {
    'fog': 'fog.png',
    'haze': 'fog.png',
    'smoke': 'fog.png',
    'clear': 'sunny.png',
    'mostly sunny': 'sunny.png',
    'sunny': 'sunny.png',
    'clear with periodic clouds': 'cloudy.png',
    'cloudy': 'cloudy.png',
    'partly cloudy': 'partly_cloudy.png',
}

root.mainloop()
