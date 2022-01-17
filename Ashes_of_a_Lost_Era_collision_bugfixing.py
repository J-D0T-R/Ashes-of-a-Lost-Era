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
WIDTH = 600
HEIGHT = 600
FPS = 30


# Colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


# Arrays
cards_list = []

zone_list = []


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

placeholder3_img = pygame.image.load(path.join(img_dir, "placeholder3.png")).convert()

 
# Set running and moving values
running = True
selection_made = False

# Classes
class Cards(pygame.sprite.Sprite):
    def __init__(self, name, image, centerx, centery):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.image = image
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = centerx
        self.rect.centery = centery
        self.selected = False
        
    def moving(self):
        if moving == True:
            print("move")
    
    def update(self):
        pass
    
    def test(self):
        print("test")
        
class Zones(pygame.sprite.Sprite):
    def __init__(self, centerx, centery):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((75, 25))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.centerx = centerx
        self.rect.centery = centery
    

## Instances

# cards
placeholder1 = Cards("placeholder1", placeholder_img, 300, 300)
cards_list.append(placeholder1)

placeholder2 = Cards("placeholder2", placeholder2_img, 200, 400)
cards_list.append(placeholder2)

placeholder3 = Cards("placeholder3", placeholder3_img, 270, 425)
cards_list.append(placeholder3)

# zones
p_zone1 = Zones(100, 100)
zone_list.append(p_zone1)


# I used this code to determine if I could acess properties and methods
# of individual instances of a class by first putting them in an array
# turns out I can!

for card in cards_list:
    Cards.test(card)
    print(card.name)


# Adding and Grouping Sprites
all_sprites = pygame.sprite.Group()
all_cards = pygame.sprite.Group()
all_zones = pygame.sprite.Group()

for card in cards_list:
    cards = Cards(card, card.image, card.rect.centerx, card.rect.centery)
    all_sprites.add(cards)
    all_cards.add(cards)
    
for zone in zone_list:
    zones = Zones(zone.rect.centerx, zone.rect.centery)
    all_sprites.add(zones)
    all_zones.add(zones)

# Game Loop
running = True
while running:
    all_sprites = pygame.sprite.Group()
    all_cards = pygame.sprite.Group()
    all_zones = pygame.sprite.Group()

    
    for card in cards_list:
        cards = Cards(card, card.image, card.rect.centerx, card.rect.centery)
        all_sprites.add(cards)
        all_cards.add(cards)
        
    for zone in zone_list:
        zones = Zones(zone.rect.centerx, zone.rect.centery)
        all_sprites.add(zones)
        all_zones.add(zones)
        
    # Maintian FPS throughout game
    clock.tick(FPS)
    # Process Input (Events)
    for event in pygame.event.get():
        # Check for closing the window
        if event.type == pygame.QUIT:
            running = False
            
        # Making the image move
        if event.type == pygame.MOUSEBUTTONDOWN and selection_made == False:
            for card in cards_list:
                if card.rect.collidepoint(event.pos):
                    selection_made = True
                    card.selected = True
                    print(card.name)
                else:
                    card.selected = False
                    
        elif event.type == pygame.MOUSEBUTTONDOWN and selection_made == True:       
            # moving the cards
            for card in cards_list:
                if card.selected == True:
                    location_x, location_y = pygame.mouse.get_pos()
                    print(location_x)
                    card.rect.centerx = location_x
                    print(location_y)
                    card.rect.centery = location_y
                    card.selected = False
                    selection_made = False
    
    # Update
    all_sprites.update()
    
    # Collision
    hits = pygame.sprite.groupcollide(all_cards, all_zones, True, True)
    if hits:
        for hit in hits:
            print("test")
        
    # Draw / Render
    screen.fill(WHITE)
    all_sprites.draw(screen)
    # Construct the border to the image
    
    # Always flip last.
    pygame.display.flip()
    
pygame.quit()