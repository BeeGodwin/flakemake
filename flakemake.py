import pygame, sys, math
from pygame.locals import *
from flake import Branch
import random

def draw_branch(branch, DSURF, weight):
    dest_x = branch.ori[0] + (branch.vec[0] * branch.leng)
    dest_y = branch.ori[1] + (branch.vec[1] * branch.leng)
    pygame.draw.line(DSURF, (255, 255, 255), branch.ori, (dest_x, dest_y), weight)
    for pair in branch.branches:
        for child_branch in pair:
            draw_branch(child_branch, DSURF, weight - 2)

def main():
    pygame.init()
    DSURF = pygame.display.set_mode((1024, 768))
    pygame.display.set_caption('FlakeMake 0.01a')
    ORIGIN = (512, 384)
    new_flake(DSURF, ORIGIN, 250, 6, 50, 0.4)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == 32:
                    new_flake(DSURF, ORIGIN, 250, 6, 50, 0.4)
        pygame.display.update()

def new_flake(DSURF, ORIGIN, l, sides, d, p):
    DSURF.fill((0,0,0))
    angle = 360 / sides
    seed = random.randrange(0, 1000000)
    for i in range(sides):
        random.seed(seed)
        branch_angle = angle * i
        vec_x, vec_y = math.sin(math.radians(branch_angle)), math.cos(math.radians(branch_angle))
        branch = Branch(ori=ORIGIN, vec=(vec_x, vec_y), leng=l, n=sides, dens=d, prob=p)
        draw_branch(branch, DSURF, 9)

if __name__ == '__main__':
    main()
