from stoked import __version__
from stoked.math import multiply_two_numbers


def test_version():
    assert __version__ == '0.1.0'

def test_multiply_two_numbers():
    assert multiply_two_numbers(2, 3) == 6
