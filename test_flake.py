from flake import Branch
import random, math, numpy

def test_init():
    pass

def test_create_nodes():
    branch = Branch(leng=30, dens=10, prob=1)
    nodes = branch.place_nodes()
    assert nodes == [(0, -10), (0, -20)]
    branch = Branch(leng=30, dens=15, prob=1)
    nodes = branch.place_nodes()
    assert nodes == [(0, -15)]
    branch = Branch(leng=100, dens=1, prob=0)
    nodes = branch.place_nodes()
    assert nodes == [] # won't work til rand does.
    branch = Branch(vec=(0, 1), leng=30, dens=15, prob=1)
    nodes = branch.place_nodes()
    assert nodes == [(0, 15)]

def test_rand_place():
    branch = Branch(prob=1)
    assert branch.rand_place() == True
    branch.prob = 0
    assert branch.rand_place() == False

def test_place_branch():
    branch = Branch(leng=20, n=4, dens=10, prob=1)
    assert len(branch.place_branches((0, -10))) == 2
    assert type(branch.place_branches((0, -10))) == list

def test_branch_gen():
    branch = Branch(leng=20, n=4, dens=10, prob=1)
    node = (0, -10)
    angles = [(1, 0), (-1, 0)]
    branch.branches = branch.branch_gen(node, angles)
    assert len(branch.branches) == 2
    assert branch.branches[0].leng == 10
    assert branch.branches[0].vec == (1, 0)
    assert branch.branches[1].vec == (-1, 0)

def test_get_angles():
    branch = Branch(n=4)
    assert branch.angles[0] == [(1, 0), (-1, 0)]
    assert len(branch.angles) == 1
    branch = Branch(n=6)
    assert branch.angles[0] == [(0.866, -0.5), (-0.866, -0.5)]
    assert branch.angles[1] == [(0.866, 0.5), (-0.866, 0.5)]
    assert len(branch.angles) == 2
    branch = Branch(n=7)
    assert len(branch.angles) == 3
    assert branch.angles[0] == [(0.782, -0.623), (-0.782, -0.623)]

def test_polar():
    branch = Branch()
    eps = 0.001
    assert abs(branch.polar((0.707, -0.707)) - 45) < eps
    assert abs(branch.polar((0.707, 0.707)) - 135) < eps
    assert abs(branch.polar((-0.707, 0.707)) - 225) < eps
    assert abs(branch.polar((-0.707, -0.707)) - 315) < eps

def test_cartesian():
    branch = Branch()
    eps = 0.001
    assert abs(branch.cartesian(45)[0] - 0.707) < eps
    assert abs(branch.cartesian(45)[1] - -0.707) < eps
    assert abs(branch.cartesian(135)[0] - 0.707) < eps
    assert abs(branch.cartesian(135)[1] - 0.707) < eps
    assert abs(branch.cartesian(225)[0] - -0.707) < eps
    assert abs(branch.cartesian(225)[1] - 0.707) < eps
    assert abs(branch.cartesian(315)[0] - -0.707) < eps
    assert abs(branch.cartesian(315)[1] - -0.707) < eps
