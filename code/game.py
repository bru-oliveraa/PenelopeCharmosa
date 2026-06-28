import pygame # realizando a importação do pygame

from code.menu import Menu
from const import WIN_WIDTH, WIN_HEIGHT


class game:
    def __init__(self):
        pygame.init()
        self.Window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.Window)
            menu.run()
            pass


