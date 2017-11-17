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
            print(event.key)
        index += 1
