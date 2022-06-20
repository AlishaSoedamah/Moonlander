import pygame
from pygame.locals import *
import time

# game vars
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
game = True
burn = False
speed_y = 0.0  # y-positive is down
speed_x = 0.0
trust = 0.15
gravity = 0.05
player_x = 299.0
player_y = 30.0
fuel = 500
fuel_color = GREEN
crash = False
landing_speed = 0.0
touch_speed = 0.0
game_height = 650
game_width = 650
game_width / 2 - player_x / 2
clock = pygame.time.Clock()

# init game window
pygame.init()
size = (game_width, game_height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Moon Shuttle touchdown")
player_off = pygame.image.load('off.bmp').convert()
player_on = pygame.image.load('on.bmp').convert()
player_crash = pygame.image.load('crash.bmp').convert()
background = pygame.image.load('space.bmp').convert()
landings_ground = pygame.image.load('landing.bmp').convert()

# colorkey = white = transparent bg
player_on.set_colorkey(WHITE)
player_off.set_colorkey(WHITE)
player_crash.set_colorkey(WHITE)
landings_ground.set_colorkey(WHITE)

# draw bg
screen.blit(background, [0, 0])

# draw landings ground
screen.blit(landings_ground, [0, 0])

# draw user sprite (lander)
screen.blit(player_off, [player_x, player_y])

# refresh game window
pygame.display.update()

# add key events so player can move
# make an (almost) endless loop
# this condition is added at the beginning of each iteration
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if pygame.key.get_pressed()[K_ESCAPE]:
            print("This is an exit by escape")
            game = False
        if pygame.key.get_pressed()[K_SPACE]:
            speed_y -= trust
            burn = True

    speed_y += gravity
    player_y += speed_y

    screen.blit(background, [0, 0])

    # draw user sprite (lander)
    screen.blit(player_off, [player_x, player_y])

    # draw landings ground
    screen.blit(landings_ground, [0, 0])
    
    # refresh the game window
    pygame.display.update()
    clock.tick(50)
    if burn == True:
        screen.blit(player_on, [player_x, player_y])
    else:
        screen.blit(player_off, [player_x, player_y])

    pygame.display.update()
    burn = False
