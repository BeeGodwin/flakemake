import pygame
from pygame.locals import *
import sys
import math
import random
from flake import Branch


# TODO need to add some GUI feedback, and to refactor to deal with the Flake obj.
# TODO some way of dealing with time, time deltas, and frame rate.
# TODO rotate stuff.
# TODO glow.
# TODO time-drawing effects.
# TODO color

def draw_branch(branch, dsurf, weight):
    dest_x = branch.ori[0] + (branch.vec[0] * branch.leng)
    dest_y = branch.ori[1] + (branch.vec[1] * branch.leng)
    pygame.draw.line(dsurf, (255, 255, 255), branch.ori, (dest_x, dest_y), weight)
    for pair in branch.branches:
        for child_branch in pair:
            draw_branch(child_branch, dsurf, weight - 2)


def main():
    pygame.init()
    dsurf = pygame.display.set_mode((1024, 768))
    pygame.display.set_caption('FlakeMake 0.02a')
    origin = (512, 384)
    ln, n, d, p = 200, 6, 40, 0.2
    new_flake(dsurf, origin, ln, n, d, p)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == 32:
                    new_flake(dsurf, origin, ln, n, d, p)
                elif event.key == 97:  # a
                    n += 1
                    n = min(n, 24)
                elif event.key == 100:  # d
                    n -= 1
                    n = max(n, 3)
                elif event.key == 119:  # w
                    p += 0.05
                    p = min(p, 0.95)
                elif event.key == 115:  # s
                    p -= 0.05
                    p = max(p, 0.05)
                elif event.key == 101:  # e
                    ln += 10
                    ln = min(ln, 350)
                    d += 2
                    d = min(d, 70)
                elif event.key == 113:  # q
                    ln -= 10
                    ln = max(ln, 80)
                    d -= 2
                    d = max(d, 16)

        pygame.display.update()


def new_flake(dsurf, origin, l, sides, d, p):
    dsurf.fill((0, 0, 0))
    angle = 360 / sides
    seed = random.randrange(random.getrandbits(32))

    for i in range(sides):
        random.seed(seed)
        branch_angle = angle * i
        vec_x, vec_y = math.sin(math.radians(branch_angle)), math.cos(math.radians(branch_angle))
        branch = Branch(ori=origin, vec=(vec_x, vec_y), leng=l, n=sides, dens=d, prob=p)
        depth = flake_depth(branch, 0)
        if depth < 3:  # NOTE get rid of magic numbers.
            new_flake(dsurf, origin, l, sides, d, p)
            break
        draw_branch(branch, dsurf, 9)


def flake_depth(branch, count):
    if len(branch.branches) == 0:
        return count
    count += 1
    return flake_depth(branch.branches[0][0], count)


if __name__ == '__main__':
    main()
