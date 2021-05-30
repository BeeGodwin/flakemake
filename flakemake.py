import random

import math
import pygame
import sys
from pygame.locals import *

from flake import Branch


def draw_branch(branch, draw_surface, weight):
    dest_x = branch.ori[0] + (branch.vec[0] * branch.leng)
    dest_y = branch.ori[1] + (branch.vec[1] * branch.leng)
    pygame.draw.line(draw_surface, (255, 255, 255), branch.ori, (dest_x, dest_y), weight)
    for pair in branch.branches:
        for child_branch in pair:
            draw_branch(child_branch, draw_surface, weight - 2)


def main():
    pygame.init()
    draw_surface = pygame.display.set_mode((1024, 768))
    pygame.display.set_caption('FlakeMake 0.01a')
    origin = (512, 384)
    branches, probability, length, density = 6, 0.2, 200, 40
    new_flake(draw_surface, origin, length, branches, density, probability)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == 32:
                    new_flake(draw_surface, origin, length, branches, density, probability)
                elif event.key == 97:  # a
                    branches += 1
                elif event.key == 100:  # d
                    branches -= 1
                elif event.key == 119:  # w
                    probability += 0.05
                    probability = min(probability, 0.95)
                elif event.key == 115:  # s
                    probability -= 0.05
                    probability = max(probability, 0.05)
                elif event.key == 101:  # e
                    length += 10
                    length = min(length, 350)
                    density += 2
                    density = min(density, 70)
                elif event.key == 113:  # q
                    length -= 10
                    length = max(length, 80)
                    density -= 2
                    density = max(density, 16)
        pygame.display.update()


def new_flake(draw_surface, origin, length, sides, density, probability):
    draw_surface.fill((0, 0, 0))
    angle = 360 / sides
    seed = random.randrange(random.getrandbits(32))

    for i in range(sides):
        random.seed(seed)
        branch_angle = angle * i
        vec_x, vec_y = math.sin(math.radians(branch_angle)), math.cos(math.radians(branch_angle))
        branch = Branch(ori=origin, vec=(vec_x, vec_y), leng=length, n=sides, dens=density, prob=probability)
        depth = flake_depth(branch, 0)
        if depth < 3:
            new_flake(draw_surface, origin, length, sides, density, probability)
            break
        draw_branch(branch, draw_surface, 9)


def flake_depth(branch, count):
    if len(branch.branches) == 0:
        return count
    count += 1
    return flake_depth(branch.branches[0][0], count)


if __name__ == '__main__':
    main()
