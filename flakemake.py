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
    new_flake(DSURF, ORIGIN, 200, 6, 40, 0.2)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == 32:
                    new_flake(DSURF, ORIGIN, 200, 6, 5, 0.2)
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
        depth = flake_depth(branch, 0)
        if depth < 3: # NOTE get rid of magic numbers.
            new_flake(DSURF, ORIGIN, l, sides, d, p)
            break
        draw_branch(branch, DSURF, 9)

def flake_depth(branch, count):
    if len(branch.branches) == 0:
        return count
    count += 1
    return flake_depth(branch.branches[0][0], count)


if __name__ == '__main__':
    main()
