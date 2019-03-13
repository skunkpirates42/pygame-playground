# Pygame second sprite Example
# This demo introduces working with sprites
# from the internet and working with the computer's
# file system to load them into our python application
import pygame
import random
import os

WIDTH = 800
HEIGHT = 600
FPS = 30

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# set up assets folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')


class Player(pygame.sprite.Sprite):
    # sprite for the Player
    def __init__(self):
        # this line is required to properly create the sprite
        pygame.sprite.Sprite.__init__(self)
        # create a plain rectangle for the sprite image
        self.image = pygame.image.load(os.path.join(img_folder, 'p1_jump.png')).convert()
        # make the rectangle around the sprite transparent
        self.image.set_colorkey(BLACK)
        # find the rectangle that encloses the image
        self.rect = self.image.get_rect()
        # center the sprite on the screen
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        # set y-axis speed -- this will be used in the update function below
        # NOTE: y-axis start at 0 at the top and gets bigger as it goes down
        self.y_speed = 5

    def update(self):
        # any code here will happen every time the game loop updates
        self.rect.x += -5
        self.rect.y += self.y_speed
        if self.rect.bottom > HEIGHT - 200:
          self.y_speed = -5
        if self.rect.top < 200:
          self.y_speed = 5
        if self.rect.right < 0:
            self.rect.left = WIDTH

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My game")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()

    # Draw / render
    screen.fill(BLUE)
    all_sprites.draw(screen)
    # *after* drawing everything, flip the display
    pygame.display.flip()
    pygame.event.get()

pygame.quit()