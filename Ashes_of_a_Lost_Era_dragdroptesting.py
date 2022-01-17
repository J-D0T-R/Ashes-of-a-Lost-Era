###   Ashes Of a Lost Era: Testing Drag and Drop  ###
###   James Rutley   ###
###   Start Date: 12/02/2021   ###
###   End Date:    ###


# Imports
import pygame
import random
import pygame_textinput

from os import path


# finding assets
img_dir = path.join(path.dirname(__file__), 'AoaLE_img')
snd_dir = path.join(path.dirname(__file__), 'AoaLE_snd')


# Constants
WIDTH = 1100
HEIGHT = 1000
FPS = 30


# Colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


# Initialization
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("placeholder")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()


# Load game Graphics
placeholder_img = pygame.image.load(path.join(img_dir, "placeholder.png")).convert()
placeholder2_img = pygame.image.load(path.join(img_dir, "placeholder2.png")).convert()


# Arrays


# Draw rectangle around the image
rect1 = placeholder_img.get_rect()
rect1.center = WIDTH//2, HEIGHT//2

rect2 = placeholder_img.get_rect()
rect1.center = WIDTH//3, HEIGHT//3 
 
# Set running and moving values
running = True
moving1 = False
moving2 = False


# Classes
class Cards(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.image = image
        self.rect = self.image.get_rect()
        self.centerx = x

# Instances
# placeholder1 = Cards()
# placeholder2 = Cards()

# Game Loop
running = True
while running:
    # Maintian FPS throughout game
    clock.tick(FPS)
    # Process Input (Events)
    for event in pygame.event.get():
        # Check for closing the window
        if event.type == pygame.QUIT:
            running = False
            
        # Making the image move
        if event.type == pygame.MOUSEBUTTONDOWN:
            if rect1.collidepoint(event.pos):
                moving1 = True

            if rect2.collidepoint(event.pos):
                moving2 = True
                
        # Set moving as False if you want
        # to move the image only with the
        # mouse click
        # Set moving as True if you want
        # to move the image without the
        # mouse click
        if event.type == pygame.MOUSEBUTTONUP:
            moving1 = False
            moving2 = False

        # Make your image move continuously
        if event.type == pygame.MOUSEMOTION and moving1:
            rect1.move_ip(event.rel)
        if event.type == pygame.MOUSEMOTION and moving2:
            rect2.move_ip(event.rel)
        
    # Update
    all_sprites.update()
    # Draw / Render
    screen.fill(WHITE)
    # Construct the border to the image
    pygame.draw.rect(screen, BLUE, rect1, 2)
    pygame.draw.rect(screen, BLUE, rect2, 2)
    # Always flip last.
    pygame.display.flip()
    
pygame.quit()