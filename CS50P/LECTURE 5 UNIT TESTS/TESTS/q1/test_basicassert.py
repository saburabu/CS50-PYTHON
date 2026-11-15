from basicassert import square as sq

def test_square():
    assert sq(2) == 4
    assert sq(5) == 25
    assert sq(0) == 0