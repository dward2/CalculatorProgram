def get_slope(p1, p2):
    m = (p2[1] - p1[1]) / (p2[0] - p1[0])
    return m


def get_intercept(point, slope):
    # y = m * x + b
    # b = y - m * x
    b = point[1] - slope * point[0]
    return b


def new_y(p1, p2, x):
    m = get_slope(p1, p2)
    b = get_intercept(p1, m)
    y = m * x + b
    return y
