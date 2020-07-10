import pygame
from pygame.locals import *

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((640, 480))
player = pygame.image.load('bug1.png').convert()
background = pygame.image.load('background.png').convert()
screen.blit(background, (0, 0))        #draw the background
position = player.get_rect()
screen.blit(player, position)          #draw the player
pygame.display.update()                #and show it all
for x in range(100):                   #animate 100 frames
    screen.blit(background, position, position) #erase
    position = position.move(2, 0)     #move player
    screen.blit(player, position)      #draw new player
    pygame.display.update()            #and show it all
    pygame.time.delay(100)             #stop the program for 1/10 second