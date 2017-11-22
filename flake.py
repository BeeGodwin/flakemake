"""FlakeMake 0.02a"""
import random
import math
import numpy

# NOTE add a Flake class that encapsulates n Branch objects.
# Flake can contain methods to manipulate the whole flake, ie. rotate,
# change color. Am thinking we probably want to look at numpy and get into the
# maths a bit?

class Branch:
    """recursively constructs one arm of a flake. Seed the RNG before you create
    the object if you want branches that look alike."""

    def __init__(self, ori=(0, 0), vec=(0, -1), leng=10, n=4, dens=10, prob=1):
        self.ori = ori  # (x, y) tuple describing pt on scr
        self.vec = vec  # (x, y) tuple describing norm vector
        self.leng = leng  # length in pixels
        self.dens = dens  # nodes are this far apart
        self.prob = prob  # 0-1 probability of nodes
        self.n = n  # sidedness of snowflake. should this be a class var?
        self.angles = self.get_angles(n)  # list of pairs of (x, y) norm vectors
        self.nodes = self.place_nodes()  # list of (x, y) points
        self.branches = []  # list of lists of Branch objects

        for node in self.nodes:
            self.branches.append(self.place_branches(node))

    def place_nodes(self):
        """returns a list of (x, y) tuples of points along this branch. dens says
        how many pixels apart nodes should be. prob is the likelihood of a given
        node being added to the returned list."""
        # print('origin {}, vec {}, len {},
        # density {}, prob {}.'.format(self.ori, self.vec, self.leng, self.dens, self.prob))
        nodes = []
        x_gap, y_gap = self.vec[0] * self.dens, self.vec[1] * self.dens
        node = (self.ori[0] + x_gap, self.ori[1] + y_gap)
        for i in range(int((self.leng // self.dens)) - 1):
            if self.choose():
                nodes.append(node)
            node = (node[0] + x_gap, node[1] + y_gap)
        return nodes

    def choose(self):
        """uses self.prob to choose true/false."""
        if self.leng < self.dens:
            return False
        if random.random() < self.prob:
            return True
        else:
            return False

    def place_branches(self, node):
        """instantiates a pair(s) of new branches at the given node, and returns
        a list of pairs of branches."""
        # branches = []
        if len(self.angles) == 1:
            branches = self.branch_gen(node, self.angles[0])
            return branches
        else:
            j = random.randrange(0, len(self.angles) - 1)
            branches = self.branch_gen(node, self.angles[j])
        return branches

    def branch_gen(self, node, angles):
        """parameterizes & instantiates one pair of new branches."""
        sd = random.randrange(random.getrandbits(32))
        _len = self.leng - self.dens
        _den = self.dens
        if self.choose():
            _len /= 2
            _den /= 2

        random.seed(sd)
        branch_a = Branch(ori=node, vec=angles[0], leng=_len, prob=self.prob, dens=_den, n=self.n)
        # print('New branch at {} with vec {} and leng {}'.format(branch_a.ori, branch_a.vec, branch_a.leng))
        random.seed(sd)
        branch_b = Branch(ori=node, vec=angles[1], leng=_len, prob=self.prob, dens=_den, n=self.n)
        # print('New branch at {} with vec {} and leng {}'.format(branch_b.ori, branch_b.vec, branch_b.leng))
        return [branch_a, branch_b]

    def get_angles(self, n):
        """returns a list of tuples of (x, y) tuples, describing normalised
        vectors of the angles that the branches off this branch will produce."""
        my_angle = self.polar(self.vec)
        pairs = (n - 1) // 2
        angles = []
        angle_inc = 360 / n
        for i in range(pairs):
            pair = [my_angle + angle_inc * (i + 1), my_angle - angle_inc * (i + 1)]
            angles.append([self.cartesian(pair[0]), self.cartesian(pair[1])])
        return angles

    @staticmethod
    def polar(vec):
        """given a normalised (x, y) vector, return its angle (with 0 being
        considered vertical, on a scale 0-359.99.)"""
        phi = math.degrees(numpy.arctan2(vec[0], -vec[1]))
        if vec[0] < 0:
            phi += 360
        return round(phi, 3)

    @staticmethod
    def cartesian(phi):
        """given an angle phi, return a normalised (x, y) vector as a tuple of
        floats."""
        x = round(math.sin(math.radians(phi)), 3)
        y = -round(math.cos(math.radians(phi)), 3)
        return x, y
