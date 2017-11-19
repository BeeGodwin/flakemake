'''FlakeMake 0.01a'''

class Branch:
    '''recursively constructs one arm of a flake. Seed the RNG before you create
    the object if you want branches that look alike.'''
    def __init__(self, ori, vec, leng, n, dens, prob):
        self.ori = ori # (x, y) tuple describing pt on scr
        self.vec = vec # (x, y) tuple describing norm vector
        self.leng = leng # length in pixels
        self.angles = self.get_angles(n)

        for node in self.place_nodes(dens, prob, leng):
            if self.rand_place_branch():
                self.place_branch(node)

    def place_nodes(self, dens, prob, leng):
        '''returns a list of (x, y) tuples of points along this branch.'''
        return []

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
        pass

def main():
    branch = Branch(ori=(0, 0), vec=(-1, 0), leng=200, n=6, dens=10, prob=1)
    print(branch)

if __name__ == '__main__':
    main()
