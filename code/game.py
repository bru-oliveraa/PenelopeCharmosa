#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame # realizando a importação do pygame

from code.menu import Menu


class Game:
    def __init__(self):
        # Inicializa o pacote do pygame;
        pygame.init()
        # Realiza a criação de uma variável com tamanho da tela que irá aparecer para o jogador;
        self.Window = pygame.display.set_mode(size=(800, 600))

    def run(self, ):
        while True:
            menu = Menu (self.Window)
            menu.run()
            pass

            # Check for all events;
            # for event in pygame.event.get():
              # if event.type == pygame.QUIT:
               # pygame.quit() # Close window;
               # quit() # End pygame