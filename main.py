# realizando a importação do pygame
import pygame

pygame.init() # Inicializa o pacote do pygame;

window = pygame.display.set_mode(size=(800, 600)) # Realiza a criação de uma variável com tamanho da tela que irá aparecer para o jogador;

while True:
# Check for all events;
 for event in pygame.event.get():
     if event.type == pygame.QUIT:
         pygame.quit() # Close window;
         quit() # End pygame

