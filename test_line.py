def test_new_y():
    from line import new_y
    pt1 = (0, 0)
    pt2 = (3, 1)
    x = 6
    result = new_y(pt1, pt2, x)
    expected = 2
    assert result == expected


def test_get_slope():
    from line import get_slope
    pt1 = (3, 0)
    pt2 = (0, 6)
    result = get_slope(pt1, pt2)
    expected = -2
    assert result == expected


def test_get_intercept():
    from line import get_intercept
    point = (-3, 10)
    slope = -1
    result = get_intercept(point, slope)
    expected = 7
    assert result == expected
