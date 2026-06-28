
import pygame

from const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION, COLOR_PINK
from const import COLOR_PURPLE
from pygame import Surface
from pygame.font import Font
from pygame import Rect


class Menu:
    def __init__(self, Window):
        self.Window = Window
        self.surf = pygame.image.load('./asset/10.png')
        self.surf = pygame.transform.scale(self.surf, (WIN_WIDTH, WIN_HEIGHT))
        self.rect = self.surf.get_rect(left=0, top = 0)


    def run(self, ):
        pygame.mixer_music.load('./asset/369920__mrthenoronha__cartoon-game-theme-loop.wav')
        pygame.mixer_music.play(-1)
        while True:

          self.Window.blit(source=self.surf, dest=self.rect)
          self.menu_text(50,"Penelope", text_color= COLOR_PURPLE, text_center_pos=((WIN_WIDTH / 2), 70))
          self.menu_text(50, "Charmosa", text_color= COLOR_PURPLE, text_center_pos=((WIN_WIDTH / 2), 120))
          for i in range(len(MENU_OPTION)):
              self.menu_text(20, MENU_OPTION[i], text_color=COLOR_PINK, text_center_pos=((WIN_WIDTH / 2), 200 + 25 *i))

          pygame.display.flip()
          # Check for all events;
          for event in pygame.event.get():
              if event.type == pygame.QUIT:
                  pygame.quit()  # Close window;
                  quit()  # End pygame

        pass

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Cooper Black", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.Window.blit(source=text_surf, dest=text_rect)

