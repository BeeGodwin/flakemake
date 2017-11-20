'''FlakeMake 0.01a'''
import random
import math
import numpy

class Branch:
    '''recursively constructs one arm of a flake. Seed the RNG before you create
    the object if you want branches that look alike.'''
    def __init__(self, ori=(0, 0), vec=(0, -1), leng=100, n=6, dens=1, prob=1):
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
        my_angle = self.polar(self.vec)
        pairs = (n - 1) // 2
        angles = []
        angle_inc = 360 / n
        for i in range(pairs):
            pair = [my_angle + angle_inc * (i + 1), my_angle - angle_inc * (i + 1)]
            angles.append([self.cartesian(pair[0]), self.cartesian(pair[1])])
        return angles

    def polar(self, vec):
        '''given a normalised (x, y) vector, return its angle (with 0 being
        considered vertical, on a scale 0-359.99.)'''
        phi = math.degrees(numpy.arctan2(vec[0], -vec[1]))
        if vec[0] < 0:
            phi += 360
        return round(phi, 3)

    def cartesian(self, phi):
        '''given an angle phi, return a normalised (x, y) vector as a tuple of
        floats.'''
        x = round(math.sin(math.radians(phi)), 3)
        y = -round(math.cos(math.radians(phi)), 3)
        return (x, y)

# def main():
#     branch = Branch(ori=(0, 0), vec=(-1, 0), leng=200, n=6, dens=10, prob=1)
#     print(branch)
#
# if __name__ == '__main__':
#     main()
