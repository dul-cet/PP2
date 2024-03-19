# 1. Create a simple clock application (only with minutes and seconds) 
# which is synchronized with system clock.
# Use Mickey's right hand as minutes arrow and left - as seconds.

import pygame
from datetime import datetime

pygame.init() 
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
CENTER = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
pygame.display.set_caption("Mickey Mouse")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

FPS = 60
clock = pygame.time.Clock()

bg = pygame.image.load(r'C:\Users\Moldir\VSCodeProjects\githowto\repositories\Lab_7\main_clock.jpg')
BG_WIDTH = 500
BG_HEIGHT = 500
BG_X_POS = (SCREEN_WIDTH / 2 - BG_WIDTH / 2)
BG_Y_POS = (SCREEN_HEIGHT / 2 - BG_HEIGHT / 2)

big_arrow = pygame.image.load(r'C:\Users\Moldir\VSCodeProjects\githowto\repositories\Lab_7\right-hand.jpg')
BIG_ARROW_WIDTH = 35
BIG_ARROW_ASPECT_RATIO = 0.12
BIG_ARROW_HEIGHT = BIG_ARROW_WIDTH / BIG_ARROW_ASPECT_RATIO
big_arrow = pygame.transform.scale(big_arrow, (BIG_ARROW_WIDTH, BIG_ARROW_HEIGHT))

small_arrow = pygame.image.load(r'C:\Users\Moldir\VSCodeProjects\githowto\repositories\Lab_7\left-hand.jpg')
SMALL_ARROW_WIDTH = 45
SMALL_ARROW_ASPECT_RATIO = 0.3
SMALL_ARROW_HEIGHT = SMALL_ARROW_WIDTH / SMALL_ARROW_ASPECT_RATIO
small_arrow = pygame.transform.scale(small_arrow, (SMALL_ARROW_WIDTH, SMALL_ARROW_HEIGHT))

big_arrow_rect = big_arrow.get_rect()
big_arrow_rect.center = CENTER

small_arrow_rect = small_arrow.get_rect()
small_arrow_rect.center = CENTER

running = True
while running:  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  angle_m = datetime.now().minute * -6
  angle = datetime.now().second * -6

  screen.fill(WHITE)
  screen.blit(bg, (BG_X_POS, BG_Y_POS))

  rotated_big_arrow = pygame.transform.rotate(big_arrow, angle)
  rotated_big_arrow_rect = rotated_big_arrow.get_rect()
  rotated_big_arrow_rect.center = big_arrow_rect.center
  screen.blit(rotated_big_arrow, rotated_big_arrow_rect)

  rotated_small_arrow = pygame.transform.rotate(small_arrow, angle_m)
  rotated_small_arrow_rect = rotated_small_arrow.get_rect()
  rotated_small_arrow_rect.center = small_arrow_rect.center
  screen.blit(rotated_small_arrow, rotated_small_arrow_rect)

  pygame.display.flip()
  clock.tick(FPS)

pygame.quit()