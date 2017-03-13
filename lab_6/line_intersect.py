def line_intersect(line1, line2):
    cords1 = line1[0] + line1[1]
    cords2 = line2[0] + line2[1]

    if cords1[0] == cords1[2] or cords2[0] == cords2[2]:
        return 'invalid function(s)'

    if k(cords1) == k(cords2):
        if b(cords1) == b(cords2):
            return line1[0]
        else:
            return None
    else:
        x = (b(cords2) - b(cords1))/(k(cords1) - k(cords2))
        y = f(x, k(cords1), b(cords1))
        return float(y), float(x)


def f(x, k, b):
    return k * x + b

def k(cords):
    x1, y1, x2, y2 = cords
    return (y2 - y1) / (x2 - x1)


def b(cords):
    x1, y1, x2, y2 = cords
    return y1 - x1 * (y2 - y1)/(x2 - x1)
