import pygame
import sys
import random
import time
from pygame.locals import *

# Initializing pygame
pygame.init()

# Setting up FPS
FPS = 60
FramePerSec = pygame.time.Clock()

# Creating colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COIN_SCORE = 0
COIN_WEIGHTS = [1, 2, 3]  # Different weights for coins

# Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load(r"C:\Users\Moldir\VSCodeProjects\githowto\repositories\Lab_8\AnimatedStreet.png")

# Create a white screen
DISPLAYSURF = pygame.display.set_mode((400, 600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

# Player class definition
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\Moldir\VSCodeProjects\githowto\repositories\Lab_8\Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

# Enemy class definition
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\Moldir\VSCodeProjects\githowto\repositories\Lab_8\Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SPEED, SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.bottom > SCREEN_HEIGHT:
            SCORE += 1
            self.reset_enemy()

    def reset_enemy(self):
        self.rect.top = 0
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# Coin class definition
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.weight = random.choice(COIN_WEIGHTS)  # Randomly select weight
        self.image = pygame.image.load(r"C:\Users\Moldir\VSCodeProjects\githowto\repositories\Lab_8\Coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global COIN_SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.bottom > SCREEN_HEIGHT:
            self.reset_coin()

    def reset_coin(self):
        self.rect.top = 0
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# Setting up Sprites
P1 = Player()
E1 = Enemy()

# Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

# Timer event for spawning coins
COIN_EVENT = pygame.USEREVENT + 2
pygame.time.set_timer(COIN_EVENT, 2000)  # Set initial time for coin spawn

# Gradual speed increment event
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 5000)  # Set initial time for speed increase
speed_increment = 0.001  # Amount of speed increase per event

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == COIN_EVENT:
            coin = Coin()
            coins.add(coin)
            all_sprites.add(coin)
        elif event.type == INC_SPEED:
            SPEED += speed_increment  # Increase speed gradually

    # Moves and Re-draws all Sprites
    DISPLAYSURF.blit(background, (0, 0))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10))

    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)

    # Handling coin collisions
    if pygame.sprite.spritecollideany(P1, coins):
        for coin in pygame.sprite.spritecollide(P1, coins, True):
            COIN_SCORE += coin.weight  # Increase coin score based on weight

    # Displaying collected coins count on the screen
    coins_text = font_small.render("Coins: " + str(COIN_SCORE), True, BLACK)
    DISPLAYSURF.blit(coins_text, (300, 10))

    # Increase enemy speed after earning certain coins
    if COIN_SCORE >= 10:
        speed_increment += 0.001  # Increase the speed increment amount

    # Game Over condition
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound(r'C:\Users\Moldir\VSCodeProjects\githowto\repositories\Lab_8\crash.wav').play()
        time.sleep(1)

        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))

        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    FramePerSec.tick(FPS)