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
WIDTH = 650
HEIGHT = 650
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
        # allows me to set the imported images as sprites.
        self.image = image
        # hides the black border around the image
        self.image.set_colorkey(BLACK)
        # creates a rect for the image
        self.rect = self.image.get_rect()
        # sets the positions for the rect
        self.rect.centerx = centerx
        self.rect.centery = centery
        # tracks if it's been clicked on
        self.selected = False
        # tracks if it's colliding with a zone
        self.in_zone = False
        
    def moving(self):
        if moving == True:
            print("move")
    
    def update(self):
        pass
    
    def test(self):
        print("test")
        
class Zones(pygame.sprite.Sprite):
    def __init__(self, name, centerx, centery):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((25, 25))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.name = name
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
# player backrow
p_zone1 = Zones("p_zone1", 110, 550)
zone_list.append(p_zone1)

p_zone2 = Zones("p_zone2", 220, 550)
zone_list.append(p_zone2)

p_zone3 = Zones("p_zone3", 330, 550)
zone_list.append(p_zone3)

p_zone4 = Zones("p_zone4", 440, 550)
zone_list.append(p_zone4)

p_zone5 = Zones("p_zone5", 550, 550)
zone_list.append(p_zone5)

# player combat zones
p_zone1c = Zones("p_zone1c", 110, 450)
zone_list.append(p_zone1c)

p_zone2c = Zones("p_zone2c", 220, 450)
zone_list.append(p_zone2c)

p_zone3c = Zones("p_zone3c", 330, 450)
zone_list.append(p_zone3c)

p_zone4c = Zones("p_zone4c", 440, 450)
zone_list.append(p_zone4c)

p_zone5c = Zones("p_zone5c", 550, 450)
zone_list.append(p_zone5c)


# I used this code to determine if I could acess properties and methods
# of individual instances of a class by first putting them in an array
# turns out I can!

for card in cards_list:
    Cards.test(card)
    print(card.name)
    
for zone in zone_list:
    print(zone.name)


# Adding and Grouping Sprites
all_sprites = pygame.sprite.Group()
all_cards = pygame.sprite.Group()
all_zones = pygame.sprite.Group()
#all_units = pygame.sprite.Group()

for card in cards_list:
    cards = Cards(card, card.image, card.rect.centerx, card.rect.centery)
    all_sprites.add(cards)
    all_cards.add(cards)
    #all_units.add(cards)
    
for zone in zone_list:
    zones = Zones(zone.name, zone.rect.centerx, zone.rect.centery)
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
        zones = Zones(zone.name, zone.rect.centerx, zone.rect.centery)
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
                if card.selected == True :
                    location_x, location_y = pygame.mouse.get_pos()
                    print(location_x)
                    card.rect.centerx = location_x
                    print(location_y)
                    card.rect.centery = location_y
                    card.selected = False
                    selection_made = False
                    card.in_zone = False
    
    # Update
    all_sprites.update()
    
    # Collision
    # Collision between cards and zones
    hits = pygame.sprite.groupcollide(all_cards, all_zones, False, True)
    for hit in hits:
        for card in cards_list:
            if card.in_zone == False and card.selected == True:
                for zone in zone_list:
                    if pygame.sprite.spritecollideany(zone, all_cards):
                        card.rect.centerx = zone.rect.centerx
                        card.rect.centery = zone.rect.centery
                        card.in_zone = True
                        card.test()
                        print(card.name)
                        print(zone.name)
                        print(card.in_zone)
            
            if card.in_zone == True and card.selected == True:
                card.in_zone = False
                print(zone.name)
    
    # Collision between cards
    #for card in cards_list:
     #   if pygame.sprite.spritecollide(card, all_cards, False):
      #      card.test()
        
    
    # Draw / Render
    screen.fill(WHITE)
    all_sprites.draw(screen)
    # Construct the border to the image
    
    # Always flip last.
    pygame.display.flip()
    
pygame.quit()