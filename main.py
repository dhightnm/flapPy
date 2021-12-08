import pygame, sys

def draw_floor():
  screen.blit(floor_surface, (floor_x_position,900))
  screen.blit(floor_surface, (floor_x_position + 576,900))


pygame.init()

screen = pygame.display.set_mode((576,1024))
clock = pygame.time.Clock()

bg_surface = pygame.transform.scale2x(pygame.image.load('assets/background-day.png').convert())
floor_surface = pygame.transform.scale2x(pygame.image.load('assets/base.png').convert())
floor_x_position = 0

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
  
  screen.blit(bg_surface, (0,0))
  floor_x_position -= 1
  draw_floor()
  if floor_x_position <= -576:
    floor_x_position = 0

  pygame.display.update()
  clock.tick(120)