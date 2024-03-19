# 3. Draw circle - a red ball of size 50 x 50 (radius = 25) on white background.
# When user presses Up, Down, Left, Right arrow keys on keyboard,
# the ball should move by 20 pixels in the direction of pressed key.
# The ball should not leave the screen,
# i.e. user input that leads the ball to leave of the screen should be ignored.

import pygame

WIDTH = 700
HEIGHT = 700

pygame.init()
pygame.display.set_caption("Red Ball")
screen = pygame.display.set_mode((WIDTH, HEIGHT))

MOVEMENT_SPEED = 20
CIRCLE_RADIUS = 25
INITIAL_X_POS , INITIAL_Y_POS = WIDTH // 2, HEIGHT // 2

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
FPS = 60

clock = pygame.time.Clock()
running = True
x = INITIAL_X_POS
y = INITIAL_Y_POS

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  pressed = pygame.key.get_pressed()

  if pressed[pygame.K_UP]:
    y = max(CIRCLE_RADIUS, y - MOVEMENT_SPEED)
  if pressed[pygame.K_DOWN]:
    y = min(HEIGHT - CIRCLE_RADIUS, y + MOVEMENT_SPEED)
  if pressed[pygame.K_LEFT]:
    x = max(CIRCLE_RADIUS, x - MOVEMENT_SPEED)
  if pressed[pygame.K_RIGHT]:
    x = min(WIDTH - CIRCLE_RADIUS, x + MOVEMENT_SPEED)

  screen.fill(WHITE)
  pygame.draw.circle(screen, RED, (x, y), CIRCLE_RADIUS)

  pygame.display.flip()
  clock.tick(FPS)

pygame.quit()