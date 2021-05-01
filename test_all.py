import main
import pytest


@pytest.mark.parametrize('digit,permutation,answer', [('baa', [0,1,2], [1,2,0]),
                                                      ('bba', [1,2,0], [2,1,0]),
                                                      ('bab', [2,1,0], [1,2,0])])
def test_step(digit,permutation,answer):
    assert answer == main.step(digit, permutation)


@pytest.fixture(params=[("3 4 1\naab\nbab\nbba\nbaa", "2 3 1"),
                        ("3 4 2\naab\nbab\nbba\nbaa", "3 2 1"),
                        ("3 4 3\naab\nbab\nbba\nbaa", "2 3 1")])
def fileout(request):
    with open('input.txt', 'w') as file:
        file.write(request.param[0])
    return request.param[1]


def test_integrate(fileout):
    main.main()
    with open('output.txt', 'r') as file:
        line = file.readline()
    assert line == fileout