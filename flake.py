'''FlakeMake 0.01a'''
import random
import math, numpy

class Branch:
    '''recursively constructs one arm of a flake. Seed the RNG before you create
    the object if you want branches that look alike.'''
    def __init__(self, ori, vec, leng, n, dens, prob):
        self.ori = ori # (x, y) tuple describing pt on scr
        self.vec = vec # (x, y) tuple describing norm vector
        self.leng = leng # length in pixels
        self.angles = self.get_angles(n)

        # for node in self.place_nodes(dens, prob, leng):
        #     if self.rand_place_branch():
        #         self.place_branch(node)

    def place_nodes(self, dens, prob, leng):
        '''returns a list of (x, y) tuples of points along this branch.'''
        pass

    def rand_place_branch(self):
        '''uses self.p to decide whether or not to place branches.
        Returns true/false.'''
        pass

    def place_branch(self, node):
        '''instantiates a pair of new branches at the given node.'''
        pass

    def get_angles(self, n):
        '''returns a list of tuples of (x, y) tuples, describing normalised
        vectors of the angles that the branches off this branch will produce.'''
        # x = round(math.sin(math.radians(i * 360 / n)), 2)
        # y = round(-math.cos(math.radians(i * 360 / n)), 2)
        # look at vec to get an angle in degrees using arcsin: (0, -1) should be vertical.
        # then work out how many angle pairs there are using n.
        # having worked them out in degrees, convert them back into vectors
        # return them as a list of pairs of tuples
        pass

    def angle(vec):
        '''given a normalised (x, y) vector, return its angle (with 0 being
        considered vertical, on a scale 0-359.99.)'''
        theta = math.degrees(numpy.arctan2(vec[0], -vec[1]))
        if vec[0] < 0:
            theta += 360
        return round(theta, 2)

# def main():
#     branch = Branch(ori=(0, 0), vec=(-1, 0), leng=200, n=6, dens=10, prob=1)
#     print(branch)
#
# if __name__ == '__main__':
#     main()
