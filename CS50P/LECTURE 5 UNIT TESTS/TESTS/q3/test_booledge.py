from booledge import is_even as ie

def test_positive_even():
    assert ie(4)
    assert ie(100)

def test_positive_odd():
    assert not ie(3)
    assert not ie(105)

def test_zero():
    assert ie(0)

def test_negative_even():
    assert ie(-4)
    assert ie(-100)

def test_negative_odd():
    assert not ie(-3)
    assert not ie(-99)