# importing libraries
import pygame
import time
import random

# Define constants
snake_speed = 13
window_x = 720
window_y = 480
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Initialize pygame
pygame.init()

# Initialise game window
pygame.display.set_caption('GeeksforGeeks Snakes')
game_window = pygame.display.set_mode((window_x, window_y))

# FPS (frames per second) controller
fps = pygame.time.Clock()

# Snake initial position and body
snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]

# Initialize fruit position and spawn flag
fruit_position = [random.randrange(1, (window_x // 10)) * 10, 
                  random.randrange(1, (window_y // 10)) * 10]
fruit_spawn = True

# Default direction of the snake
direction = 'RIGHT'
change_to = direction

# Initial score and level
score = 0
level = 1
level_up = False  # Flag to check if level has been increased

# Function to display score
def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score) + '   Level : ' + str(level), True, color)
    score_rect = score_surface.get_rect()
    score_rect.midtop = (window_x / 2, 10)
    game_window.blit(score_surface, score_rect)

# Function to display game over screen
def game_over():
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render('Your Score is : ' + str(score), True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_x / 2, window_y / 4)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # If two keys pressed simultaneously, only one should change direction
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Update snake position based on direction
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    # Check for border collision
    if snake_position[0] < 0 or snake_position[0] > window_x - 10 \
            or snake_position[1] < 0 or snake_position[1] > window_y - 10:
        game_over()

    # Snake body growing mechanism
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10
        fruit_spawn = False
    else:
        snake_body.pop()
        
    # Generate new fruit position if old one was consumed
    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x // 10)) * 10, 
                          random.randrange(1, (window_y // 10)) * 10]
    fruit_spawn = True
    
    # Increase level when score reaches multiple of 40
    if score != 0 and score % 40 == 0 and not level_up:
        level += 1
        snake_speed += 1
        level_up = True  # Set flag to prevent multiple level increments
    elif score % 40 != 0:  # Reset flag when score is not a multiple of 40
        level_up = False

    # Fill the game window with black color
    game_window.fill(black)
    
    # Draw snake and fruit on the screen
    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, white, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))

    # Check for collision with snake body
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    # Display score and level
    show_score(1, white, 'times new roman', 20)

    # Refresh game screen
    pygame.display.update()

    # Control frame rate
    fps.tick(snake_speed)