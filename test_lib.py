from lib import average

def test_average():
    assert average([10, 20, 30]) == 20
    assert average([-10, 10]) == 0
    assert average([5]) == 5
