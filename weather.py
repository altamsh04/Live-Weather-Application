from tkinter import *
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup as bs

root = Tk()
root.geometry("430x480")
root.config(background='#1C2833')
root.title("Weather Application")

photoicon = PhotoImage(file = "partly_cloudy.png")
root.iconphoto(False, photoicon)


	
def main(para):
	url = f"https://www.google.com/search?q={para.replace(' ','')}+weather"
	session = requests.Session()
	session.headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/91.0.864.59"
	html = session.get(url)

	soup = bs(html.text, "html.parser")

	wname = soup.find('span', attrs={'id':'wob_dc'}).text
	temp = soup.find('span', attrs={'id':'wob_tm'}).text
	time = soup.find('div', attrs={'id':'wob_dts'}).text

	pp = soup.find('span', attrs={'id':'wob_pp'}).text
	hm = soup.find('span', attrs={'id':'wob_hm'}).text
	ws = soup.find('span', attrs={'id':'wob_ws'}).text
	namec = soup.find('span', attrs={'class':'BBwThe'})
	loc = namec.string

	print("Okkkkkkkk")


	timeurl = f"https://www.google.com/search?q=current+time+in+{para.replace(' ','')}"
	timesession = requests.Session()
	timesession.headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/91.0.864.59"
	timehtml = timesession.get(timeurl)
	
	timesoup = bs(timehtml.text, "html.parser")
	citytime = timesoup.find('div', attrs={'class':'gsrt vk_bk FzvWSb YwPhnf'})
	realtime = citytime.string
	print("Realtime okkk")


	return wname, temp, time, pp, hm, ws, loc, realtime


def  fun():

	if len(text.get()) != 0:
		
		wname, temp, time, pp, hm, ws, loc, realtime = main(text.get())

		t1.config(text = wname)
		t2.config(text = "Current time "+realtime)
		t3.config(text = time)
		t4.config(text = "Precipitation: "+pp)
		t5.config(text = "Humidity: "+hm)
		t6.config(text = "Wind: "+ws)
		t0.config(text = loc)
		print("Okkkkkkkk2")
		print("Time is "+realtime)
		tempt.config(text=temp+"°C")

		imgstr = wname.lower()

		print(imgstr)

		if (imgstr == 'fog'):
			img.config(file = 'fog.png')

		if (imgstr == 'haze'):
			img.config(file = 'fog.png')
		
		if (imgstr == 'smoke'):
			img.config(file = 'fog.png')
		
		if (imgstr == 'clear'):
			img.config(file = 'sunny.png')

		if (imgstr == 'mostly sunny'):
			img.config(file = 'sunny.png')

		if (imgstr == 'sunny'):
			img.config(file = 'sunny.png')

		if (imgstr == 'clear with periodic clouds'):
			img.config(file = 'cloudy.png')

		if (imgstr == 'cloudy'):
			img.config(file = 'cloudy.png')
		
		if (imgstr == 'partly cloudy'):
			img.config(file = 'partly_cloudy.png')
		
		if (imgstr == 'clear'):
			print("Clear")
		else:
			print("img no")

	else:
		messagebox.showinfo(title='Warning message',message='Please enter above filled :(')


title = Label(text="Weather Application",font='Consolas 15 bold' ,fg='#45B4FF' ,bg='#1C2833')
title.place(x=80,y=10)

label = Label(text="City Name :",font='Consolas 10 bold' ,fg='#45B4FF' ,bg='#1C2833')
label.place(x=15,y=80)

text = Entry(font='Consolas 9 bold' ,fg='#1C2833')
text.place(x=130,y=80)

btn = Button(text="Find Weather",font='Consolas 9 bold' ,fg='black', bg='#45B4FF',command=fun)
btn.place(x=310,y=75)


img = PhotoImage()

imgt = Label(root, image = img,bg='#1C2833')
imgt.place(x=130,y=140)

tempt = Label(root,font='Consolas 22 bold' ,fg='#45B4FF' ,bg='#1C2833')
tempt.place(x=220,y=150)

t0 = Label(root,font='Consolas 10 bold' ,fg='#45B4FF' ,bg='#1C2833')
t0.place(x=30,y=250)

t1 = Label(root, font='Consolas 10 bold' ,fg='#45B4FF' ,bg='#1C2833')
t1.place(x=30,y=280)

t2 = Label(root, font='Consolas 10 bold' ,fg='#45B4FF' ,bg='#1C2833')
t2.place(x=30,y=310)

t3 = Label(root, font='Consolas 10 bold' ,fg='#45B4FF' ,bg='#1C2833')
t3.place(x=30,y=340)

t4 = Label(root, font='Consolas 10 bold' ,fg='#45B4FF' ,bg='#1C2833')
t4.place(x=30,y=370)

t5 = Label(root, font='Consolas 10 bold' ,fg='#45B4FF' ,bg='#1C2833')
t5.place(x=30,y=400)

t6 = Label(root, font='Consolas 10 bold' ,fg='#45B4FF' ,bg='#1C2833')
t6.place(x=30,y=430)

root.mainloop() 