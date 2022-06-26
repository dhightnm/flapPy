from random import random
import pygame, sys

def draw_floor():
  screen.blit(floor_surface, (floor_x_position,900))
  screen.blit(floor_surface, (floor_x_position + 576,900))


pygame.init()

screen = pygame.display.set_mode((576,1024))
clock = pygame.time.Clock()

#game var
gravity = 0.25
bird_movement = 0

bg_surface = pygame.transform.scale2x(pygame.image.load('assets/background-day.png').convert())
floor_surface = pygame.transform.scale2x(pygame.image.load('assets/base.png').convert())
floor_x_position = 0

bird_surface = pygame.transform.scale2x(pygame.image.load('assets/Ryen.png').convert())
bird_rect = bird_surface.get_rect(center = (100, 512))

pipe_bottom = pygame.transform.scale2x(pygame.image.load('assets/pipe-green.png').convert())
pipe_btm_rect = pipe_bottom.get_rect(topleft = (0, 512))
pipe_btm_position = range(0, 512)

def add_bottom_pipe():
  screen.blit(pipe_bottom, (pipe_btm_position, pipe_btm_position))

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        bird_movement = 0
        bird_movement -= 12
  add_bottom_pipe()
  screen.blit(bg_surface, (0,0))
  

  bird_movement += gravity
  bird_rect.centery += bird_movement
  screen.blit(bird_surface, bird_rect)
  floor_x_position -= 1
  draw_floor()
  if floor_x_position <= -576:
    floor_x_position = 0
 

  pygame.display.update()
  clock.tick(120)