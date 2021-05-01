import main
import pytest


@pytest.mark.parametrize('digit,permutation,answer', [('baa', [0,1,2], {'a': 0, 'b': 2})])
def test_step(digit,permutation,answer):
    assert answer == main.step(digit, permutation)