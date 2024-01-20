def sqrt(n: float):
    r = n/2.0
    n = float(n)
    i = 0
    while i <= 10:
        r = (r+n/r)/2.0
        i += 1
    return r


def power_two(n: float) -> float:
    return n * n
