import pygame
import sys

pygame.display.init()
screen = pygame.display.set_mode ( ( 320 , 240 ) )
index = 0

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            print("{0}: You pressed {1:c}".format ( index , event.key ))
        elif event.type == pygame.KEYUP:
            print("{0}: You released {1:c}".format ( index , event.key ))
        index += 1
