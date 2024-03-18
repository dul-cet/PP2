# 3. Draw circle - a red ball of size 50 x 50 (radius = 25) on white background.
# When user presses Up, Down, Left, Right arrow keys on keyboard,
# the ball should move by 20 pixels in the direction of pressed key.
# The ball should not leave the screen,
# i.e. user input that leads the ball to leave of the screen should be ignored.

import pygame
import sys
pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball")

WHITE = (255, 255, 255)
RED = (255, 0, 0)

ball_radius = 25
ball_x, ball_y = WIDTH // 2, HEIGHT // 2

MOVE_DISTANCE = 30

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        ball_y = max(ball_y - MOVE_DISTANCE, ball_radius)
    elif keys[pygame.K_DOWN]:
        ball_y = min(ball_y + MOVE_DISTANCE, HEIGHT - ball_radius)
    elif keys[pygame.K_LEFT]:
        ball_x = max(ball_x - MOVE_DISTANCE, ball_radius)
    elif keys[pygame.K_RIGHT]:
        ball_x = min(ball_x + MOVE_DISTANCE, WIDTH - ball_radius)

    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)
    pygame.display.flip()

pygame.quit()