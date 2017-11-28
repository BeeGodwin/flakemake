from flakemake import *
import random


def test_get_colour():
    assert get_colour((0, 0, 0), (255, 255, 255), t=0.5) == (127, 127, 127)
    assert get_colour((255, 255, 255), (0, 0, 0), t=0.5) == (127, 127, 127)
    assert get_colour((0, 0, 0), (10, 10, 10), t=0.5) == (5, 5, 5)
    assert get_colour((10, 10, 10), (0, 0, 0), t=0.5) == (5, 5, 5)
    assert get_colour((20, 20, 20), (10, 10, 10), t=0.5) == (15, 15, 15)
    random.seed(1)  # next random.random() returns 0.13436424411240122
    assert get_colour((0, 0, 0), (255, 255, 255), rand=True) == (34, 34, 34)

def test_tween():
    assert tween(0, 10, 0.5) == 5
    assert tween(10, 0, 0.5) == 5
