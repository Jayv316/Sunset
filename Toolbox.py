import os
import sys
import pygame
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
        screen = pygame.display.set_mode((w, h))
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
