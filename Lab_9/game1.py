import pygame 
import random
pygame.init()

W, H = 1200, 800
FPS = 60

screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
clock = pygame.time.Clock()
done = False
bg = (0, 0, 0)

# Game settings
game_settings = {
    'paddleSpeed': 20,
    'ballSpeed': 6,
    'blockDensity': 10,
    'blockSize': (100, 50)
}

# Paddle
paddleW = 150
paddleH = 25
paddle = pygame.Rect(W // 2 - paddleW // 2, H - paddleH - 30, paddleW, paddleH)

# Ball
ballRadius = 20
ball_rect = int(ballRadius * 2 ** 0.5)
ball = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect)
dx, dy = 1, -1

# Game score
game_score = 0
game_score_fonts = pygame.font.SysFont('comicsansms', 40)
game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (0, 0, 0))
game_score_rect = game_score_text.get_rect()
game_score_rect.center = (210, 20)

# Catching sound
collision_sound = pygame.mixer.Sound(r'C:\Users\Moldir\VSCodeProjects\githowto\repositories\Lab_9\catch.mp3')

def detect_collision(dx, dy, ball, rect):
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top

    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    if delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy

def create_blocks():
    block_list = []
    color_list = []
    for i in range(game_settings['blockDensity']):
        for j in range(4):
            block = pygame.Rect(10 + i * (game_settings['blockSize'][0] + 10), 50 + j * (game_settings['blockSize'][1] + 10),
                               game_settings['blockSize'][0], game_settings['blockSize'][1])
            block_list.append(block)
            color_list.append((random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)))
    return block_list, color_list

# Initialize blocks
block_list, color_list = create_blocks()

# Game over Screen
losefont = pygame.font.SysFont('comicsansms', 40)
losetext = losefont.render('Game Over', True, (255, 255, 255))
losetextRect = losetext.get_rect()
losetextRect.center = (W // 2, H // 2)

# Win Screen
winfont = pygame.font.SysFont('comicsansms', 40)
wintext = winfont.render('You win yay', True, (0, 0, 0))
wintextRect = wintext.get_rect()
wintextRect.center = (W // 2, H // 2)

# Settings Menu
def settings_menu():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_p:  # Change paddle speed
                    game_settings['paddleSpeed'] += 5
                elif event.key == pygame.K_b:  # Change ball speed
                    game_settings['ballSpeed'] += 1
                elif event.key == pygame.K_d:  # Change block density
                    game_settings['blockDensity'] += 5
                    block_list, color_list = create_blocks()  # Update block list after density change
        
        screen.fill(bg)
        settings_text = game_score_fonts.render(f'Paddle Speed: {game_settings["paddleSpeed"]}, Ball Speed: {game_settings["ballSpeed"]}, Block Density: {game_settings["blockDensity"]}', True, (255, 255, 255))
        screen.blit(settings_text, (100, 100))
        pygame.display.flip()
        clock.tick(FPS)

# Flag to track whether settings menu is open
settings_open = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            if not settings_open:
                settings_menu()
                settings_open = True
            else:
                settings_open = False

    screen.fill(bg)
    [pygame.draw.rect(screen, color_list[color], block) for color, block in enumerate(block_list)]  # drawing blocks
    pygame.draw.rect(screen, pygame.Color(255, 255, 255), paddle)
    pygame.draw.circle(screen, pygame.Color(255, 0, 0), ball.center, ballRadius)

    ballSpeed = game_settings['ballSpeed']
    paddleSpeed = game_settings['paddleSpeed']

    ball.x += ballSpeed * dx
    ball.y += ballSpeed * dy

    if ball.centerx < ballRadius or ball.centerx > W - ballRadius:
        dx = -dx
    if ball.centery < ballRadius + 50: 
        dy = -dy
    if ball.colliderect(paddle) and dy > 0:
        dx, dy = detect_collision(dx, dy, ball, paddle)

    hitIndex = ball.collidelist(block_list)
    if hitIndex != -1:
        hitRect = block_list.pop(hitIndex)
        hitColor = color_list.pop(hitIndex)
        dx, dy = detect_collision(dx, dy, ball, hitRect)
        game_score += 1
        collision_sound.play()
        
    game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (255, 255, 255))
    screen.blit(game_score_text, game_score_rect)
    
    if ball.bottom > H:
        screen.fill((0, 0, 0))
        screen.blit(losetext, losetextRect)
    elif not len(block_list):
        screen.fill((255, 255, 255))
        screen.blit(wintext, wintextRect)

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddleSpeed
    if key[pygame.K_RIGHT] and paddle.right < W:
        paddle.right += paddleSpeed

    pygame.display.flip()
    clock.tick(FPS)