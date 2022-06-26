import pygame, sys, random

def draw_floor():
  screen.blit(floor_surface, (floor_x_position,900))
  screen.blit(floor_surface, (floor_x_position + 576,900))

def create_pipe():
  random_pipe_pos = random.choice(pipe_height)
  new_pipe = pipe_sfc.get_rect(midtop = (700, random_pipe_pos))
  return new_pipe

def move_pipes(pipes):
  for pipe in pipes:
    pipe.centerx -= 5
  return pipes

def draw_pipes(pipes):
  for pipe in pipes:
    screen.blit(pipe_sfc, pipe)

pygame.init()

screen = pygame.display.set_mode((576,1024))
clock = pygame.time.Clock()

#game var
gravity = 0.25
bird_movement = 0

bg_surface = pygame.transform.scale2x(pygame.image.load('assets/background-day.png').convert())
floor_surface = pygame.transform.scale2x(pygame.image.load('assets/base.png').convert())
floor_x_position = 0

bird_surface = pygame.transform.scale2x(pygame.image.load('assets/bluebird-midflap.png').convert())
bird_rect = bird_surface.get_rect(center = (100, 512))

pipe_sfc = pygame.transform.scale2x(pygame.image.load('assets/pipe-green.png').convert())
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)
pipe_height = [200, 400, 600, 800]

game_start = False

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        game_start = True
        bird_movement = 0
        bird_movement -= 12
      if event.key == pygame.K_q:
        pygame.quit()
        sys.exit()
    if event.type == SPAWNPIPE:
      pipe_list.append(create_pipe())
      print(pipe_list)

  
  screen.blit(bg_surface, (0,0))

  if game_start == True:
    bird_movement += gravity
    bird_rect.centery += bird_movement

  screen.blit(bird_surface, bird_rect)
  
  pipe_list = move_pipes(pipe_list)
  draw_pipes(pipe_list)

  floor_x_position -= 1
  draw_floor()
  if floor_x_position <= -576:
    floor_x_position = 0
  pygame.display.update()
  clock.tick(120)