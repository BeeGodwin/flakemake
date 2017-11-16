import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((800, 600))
pygame.display.set_caption('FlakeMake 0.00a')

WHITE = (255, 255, 255)

origin = (400, 300)

pygame.draw.line(DISPLAYSURF, WHITE, origin, (origin[0] - 50, origin[1]), 4) # left horizontal
pygame.draw.line(DISPLAYSURF, WHITE, origin, (origin[0] + 50, origin[1]), 4) # right horizontal
pygame.draw.line(DISPLAYSURF, WHITE, origin, (origin[0], origin[1] - 50), 4) # up vertical
pygame.draw.line(DISPLAYSURF, WHITE, origin, (origin[0], origin[1] + 50), 4) # down vertical


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()


# make a snowflake.

    # get some parameters:
        # let n be the number of initial branches
        # let l be the length of a branch
        # let a be the min segment size
        # let b be the max segment size
        # let d be the branch density
        # let s be the RNG seed.

    # set up a screen space.
        # origin is in the centre of the screen

    # initialise with n branches radiating from the origin

    # populate the branches: for all branches,
        # seed rng with s
        # branch divides into segments
            # a given branch's segments are randomly in the range (a, b)
        # depending on d, start a new branch from a random point in the seg.
            # at an angle computed from n, ruling out vectors parallel to this.
            # recurse

    # functions:
        # segment(branch)
            # divides a branch's vector into a list of vectors
            # randomly call make_branch on each segment, depending on d
        # snowflake(n, l, a, b, d, s)
            # draws initial branches
            # returns an array of vectors from the origin
            # iterates over those vectors (branches)
                # seed rng with s
                # segment, starting the recursion
        # make_branch(branch, segment, n)
            # makes a new branch off this segment of this branch
            # pass to get_branch_vector for origin, direction
            # draw a branch with length derived from parent branch
            # segment that branch

        # get_branch_vector(segment)
            # given a segment, randomly generates an origin point and a vector
            # for a new branch.

        # some IO stuff I don't know how to do yet!

        # draw a line on the screen - easy enough, but we want to draw from
        # some origin point with a length, so we need to compute our start
        # and end screen coordinates. (eg if surface dim 800x600 then orig. is
        # (400, 300) but we might also be taking any point on any branch as orig.)
        # want to be able to draw with an origin, normalised direction vector
        # (which I think we can get from the trig functions) and then multiply
        # that by some length.
