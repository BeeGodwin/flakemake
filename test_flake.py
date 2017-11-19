from flake import Branch
import random, math, numpy

def test_create_nodes():
    pass

def test_rand_place_branch():
    pass

def test_place_branch():
    pass

def test_get_angles():
    branch = Branch(ori=(0,0), vec=(0, -1), leng=100, n=4, dens=1, prob=1)
    branch.get_angles(4)
    #assert branch.angles[0] == [(-1, 0), (1, 0)]

def test_angle():
    assert Branch.angle((0, -1)) == 0
    assert Branch.angle((0.707106, -0.707106)) == 45
    assert Branch.angle((1, 0)) == 90
    assert Branch.angle((0.707106, 0.707106)) == 135
    assert Branch.angle((0, 1)) == 180
    assert Branch.angle((-0.707106, 0.707106)) == 225
    assert Branch.angle((-1, 0)) == 270
    assert Branch.angle((-0.707106, -0.707106)) == 315
