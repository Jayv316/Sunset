from PIL import Image
import pygame
from Toolbox import PygameTools
def fullpath(relative_path):
	try:
		from sys import _MEIPASS
		base_path = _MEIPASS
	except Exception:
		from os.path import abspath
		base_path = abspath(".")
	from os.path import join
	return join(base_path, relative_path)
class Main():
	def __init__(self, size, title, icon_path, fps):
		self.screen = PygameTools.makescreen(size[0], size[1], title, icon_path)
		self.font = pygame.font.Font(fullpath("data/font.ttf"), 24)
		self.cycle = Image.open(fullpath("data/cycle.png"))
		self.phase = 0
		self.fps = fps
		self.running = True
		self.main()
	def main(self):
		def exit(exit_code = ""):
			from sys import exit
			pygame.quit()
			self.running = False
			exit(str(exit_code) if len(exit_code) > 0 else None)
		def gradient(col1, col2, size):
			diff = (max(col1[0], col2[0])-min(col1[0], col2[0]), max(col1[1], col2[1])-min(col1[1], col2[1]), max(col1[2], col2[2])-min(col1[2], col2[2]))
			mid = (min(col1[0], col2[0])+round(diff[0]/2), min(col1[1], col2[1])+round(diff[1]/2), min(col1[2], col2[2])+round(diff[2]/2))
			image = Image.new("RGB", size, mid)
			top = Image.new("RGB", size, col1)
			bottom = Image.new("RGB", size, col2)
			topgrad = Image.linear_gradient("L").resize(size).rotate(180)
			bottomgrad = topgrad.rotate(180)
			image.paste(top, (0, 0, size[0], size[1]), topgrad)
			image.paste(bottom, (0, 0, size[0], size[1]), bottomgrad)
			return image
		def getdetailed():
			nextphase = self.phase+1 if not self.phase == self.cycle.width-1 else 0
			topdetailtop = self.cycle.getpixel((self.phase, 0))
			topdetailbottom = self.cycle.getpixel((nextphase, 0))
			topdetailimage = gradient(topdetailtop, topdetailbottom, (60, 60)).rotate(90).resize((60, 1))
			bottomdetailtop = self.cycle.getpixel((self.phase, 1))
			bottomdetailbottom = self.cycle.getpixel((nextphase, 1))
			bottomdetailimage = gradient(bottomdetailtop, bottomdetailbottom, (60, 60)).rotate(90).resize((60, 1))
			detailimage = Image.new("RGB", (60, 2), (0, 0, 0))
			detailimage.paste(topdetailimage, (0, 0, 60, 1))
			detailimage.paste(bottomdetailimage, (0, 1, 60, 2))
			return detailimage
		tick = 0
		detailimage = getdetailed()
		paused = False
		mouse = False
		pos = (0, 0)
		while self.running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					exit()
				if event.type == 1025 or event.type == 1026:
					mouse = True if event.type == 1025 else False
			if tick >= 45-(self.cycle.width-45):
				tick = 0
				self.phase += 1
				if self.phase >= self.cycle.width:
					self.phase = 0
				detailimage = getdetailed()
			gradcoltop = detailimage.getpixel((tick, 0))
			gradcolbottom = detailimage.getpixel((tick, 1))
			gradimage = gradient(gradcoltop, gradcolbottom, (800, 800))
			gradimagepyg = pygame.image.fromstring(gradimage.tobytes(), (800, 800), "RGB")
			PygameTools.image(self.screen, gradimagepyg, 0, 0, 800, 800)
			PygameTools.makesquare(self.screen, 800, 0, 200, 800, 115, 115, 115)
			PygameTools.makesquare(self.screen, 815, 15, 170, 50, 200, 200, 200)
			pausetext = ""
			if paused:
				pausetext = "Unpause"
			else:
				pausetext = "Pause"
			PygameTools.centeredtext(self.font, self.screen, pausetext, 815, 15, 170, 50, 255, 255, 255)
			PygameTools.makesquare(self.screen, 815, 80, 170, 50, 200, 200, 200)
			PygameTools.centeredtext(self.font, self.screen, "Save", 815, 80, 170, 50, 255, 255, 255)
			PygameTools.makesquare(self.screen, 815, 155, (45-(self.cycle.width-45))*2+10, 10, 200, 200, 200)
			PygameTools.makesquare(self.screen, 815+(tick*2), 145, 10, 30, 130, 130, 130)
			PygameTools.text(self.font, self.screen, f"{tick}", 950, 145, 255, 255, 255)
			PygameTools.makesquare(self.screen, 815, 200, self.cycle.width*2+10, 10, 200, 200, 200)
			PygameTools.makesquare(self.screen, 815+(self.phase*2), 190, 10, 30, 130, 130, 130)
			PygameTools.text(self.font, self.screen, f"{self.phase}", 950, 190, 255, 255, 255)
			if mouse:
				pos = pygame.mouse.get_pos()
				if pos[0] > 815 and pos[0] < 985:
					if pos[1] > 15 and pos[1] < 65:
						paused = not paused
						mouse = False
					elif pos[1] > 80 and pos[1] < 130:
						gradimage.save("SunsetImage.png")
						mouse = False
					elif pos[1] > 145 and pos[1] < 175 and pos[0] < 815+(45-(self.cycle.width-45))*2+10:
						tick = int((round((pos[0]-815)/10, 1)*10)/2)
						if tick >= 45-(self.cycle.width-45): tick = (45-(self.cycle.width-45))-1
						if tick < 0: tick = 0
						detailimage = getdetailed()
					elif pos[1] > 190 and pos[1] < 220 and pos[0] < 815+self.cycle.width*2+10:
						self.phase = int((round((pos[0]-815)/10, 1)*10)/2)
						if self.phase >= self.cycle.width: self.phase = self.cycle.width-1
						if self.phase < 0: self.phase = 0
						detailimage = getdetailed()
			pygame.display.update()
			pygame.time.Clock().tick(self.fps)
			if not paused:
				tick += 1

if __name__ == "__main__":
	Main((1000, 800), "Sunset", "data/sunset.png", 24)