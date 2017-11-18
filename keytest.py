import pygame
import sys

pygame.display.init()
screen = pygame.display.set_mode((320, 240))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            print(event.key)
