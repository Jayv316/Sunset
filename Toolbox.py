import os
import sys
import pygame
import requests
import json
import time
import datetime
pygame.init()
pygame.font.init()
pygame.display.init()
class PygameTools():
	def makescreen(w, h, title, relative_icon_path):
		if not relative_icon_path == False and not relative_icon_path == "":
			try:
				base_path = sys._MEIPASS
			except Exception:
				base_path = os.path.abspath(".")
			path = os.path.join(base_path, relative_icon_path)
			icon = pygame.image.load(path)
		screen = pygame.display.set_mode((w,h))
		pygame.display.set_caption(title)
		if not relative_icon_path == False and not relative_icon_path == "":
			pygame.display.set_icon(icon)
		return screen
	def changetitle(title):
		pygame.display.set_caption(title)
	def changeicon(relative_icon_path):
		try:
			base_path = sys._MEIPASS
		except Exception:
			base_path = os.path.abspath(".")
		path = os.path.join(base_path, relative_icon_path)
		icon = pygame.image.load(path)
		pygame.display.set_icon(icon)
	def loadfont(relative_path, size):
		try:
			base_path = sys._MEIPASS
		except Exception:
			base_path = os.path.abspath(".")
		path = os.path.join(base_path, relative_path)
		return pygame.font.Font(path, size)
	def loadimg(relative_path):
		try:
			base_path = sys._MEIPASS
		except Exception:
			base_path = os.path.abspath(".")
		path = os.path.join(base_path, relative_path)
		return pygame.image.load(path)
	def text(font, screen, text, x, y, r, g, b):
		text_surface = font.render(text, True, (r, g, b))
		screen.blit(text_surface, (x, y))
	def image(screen, image, x, y, w, h):
		image = pygame.transform.scale(image, (w, h))
		screen.blit(image, (x, y))
	def centeredtext(font, screen, text, x, y, w, h, r, g, b):
		fontsize = font.size(text)
		text_surface = font.render(text, True, (r, g, b))
		xoffset = (w/2)-(fontsize[0]/2)
		yoffset = (h/2)-(fontsize[1]/2)
		screen.blit(text_surface, (x+xoffset, y+yoffset))
	def makesquare(screen, x, y, w, h, r, g, b):
		square = pygame.Surface((w, h))
		square.fill((r, g, b))
		screen.blit(square, (x, y))
		return [x, y, w, h]
class PythonTools():
	def loadfile(relative_path):
		try:
			base_path = sys._MEIPASS
		except Exception:
			base_path = os.path.abspath(".")
		return os.path.join(base_path, relative_path)
	def listdir(path):
		return os.listdir(path)
	def getweather(location, apikey):
		wetURL = "https://api.openweathermap.org/data/2.5/weather?q=" + location + "&units=metric&appid=" + apikey
		response = requests.get(wetURL)
		if response.status_code == 200:
			data = response.json()
			main = data['main']
			tempc = main['temp']
			humidity = main['humidity']
			pressure = main['pressure']
			report = data['weather']
			tempf = (tempc*1.8)+32
			tempf = round(tempf, 2)
			wetData = [f"{location:-^30}", f"Temperature: F:{tempf}, C:{tempc}", f"Humidity: {humidity}", f"Pressure: {pressure}", f"Weather Report: {report[0]['description']}"]
			return wetData
		else:
			return False
	def getcity(ip):
		request_url = 'https://geolocation-db.com/jsonp/' + ip
		response = requests.get(request_url)
		result = response.content.decode()
		result = result.split("(")[1].strip(")")
		result  = json.loads(result)
		city = result['city']
		return city
	def getip():
		return requests.get('https://api.ipify.org').text
	def gettime():
		return time.strftime("%I:%M:%S %p")
	def getdate():
		return datetime.datetime.now().strftime("%A %B %d, %Y")
	def getsystemusers():
		usersdir = os.listdir("C:/Users")
		usersnonwindows = []
		userswindows = []
		users = []
		for user in usersdir:
			if not user == "desktop.ini":
				if not user.startswith("Default") and not user.startswith("Public") and not user == "All Users":
					usersnonwindows.append(user)
				else:
					userswindows.append(user)
		users.append(userswindows)
		users.append(usersnonwindows)
		return users