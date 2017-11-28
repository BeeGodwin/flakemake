import pygame
from pygame.locals import *
import sys
import math
import random
from flake import Branch


def draw_branch(branch, dsurf, weight):
    """draws a branch, and then recurses thru all child branches."""
    col_a = (127, 127, 255)
    col_b = (225, 225, 255)
    end_x = branch.ori[0] + (branch.vec[0] * branch.leng)
    end_y = branch.ori[1] + (branch.vec[1] * branch.leng)
    random.seed(random.getrandbits(32))
    colour = get_colour(col_a, col_b, random.random())
    pygame.draw.line(dsurf, colour, branch.ori, (end_x, end_y), weight)
    for pair in branch.branches:
        for child_branch in pair:
            draw_branch(child_branch, dsurf, weight - 1)


def get_colour(col_a: color, col_b: color, rand=False, t=0.5):
    """returns a random colour tweened between colA and colB if random, or uses t
    where 0 >= t >= 1 to find a colour on a gradient between."""
    if rand:
        t = random.random()
    r_a, g_a, b_a = col_a
    r_b, g_b, b_b = col_b
    r_delta = tween(r_a, r_b, t)  # change to tween(int, int, t) function.
    g_delta = tween(g_a, g_b, t)
    b_delta = tween(b_a, b_b, t)
    return int(r_delta), int(g_delta), int(b_delta)


def tween(a, b, t):
    if a < b:
        a, b = b, a
    return b + (a - b) * t


def main():
    pygame.init()
    surf = pygame.display.set_mode((1024, 768))
    pygame.display.set_caption('FlakeMake 0.02a')
    origin = (512, 384)
    ln, n, d, p = 200, 6, 40, 0.2
    new_flake(surf, origin, ln, n, d, p)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == 32:
                    new_flake(surf, origin, ln, n, d, p)
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
