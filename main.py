import pygame
import platform
if platform.system() == "LINUX":

  pygame.init()

  screen = pygame.display.set_mode((576,1024))

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        False   
    pygame.display.update()