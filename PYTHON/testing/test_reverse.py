from reverse_string import reverse

def test_reverse():
    assert reverse(1234)

def test_reverse_negative():
    assert reverse(-1234)

def test_reverse_zero():
    assert reverse(0)