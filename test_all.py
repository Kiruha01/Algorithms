import main
import pytest


@pytest.mark.parametrize('digit,permutation,answer', [('baa', [0,1,2], [1,2,0]),
                                                      ('bba', [1,2,0], [2,1,0]),
                                                      ('bab', [2,1,0], [1,2,0])])
def test_step(digit,permutation,answer):
    assert answer == main.step(digit, permutation)