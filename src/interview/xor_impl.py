def xor(a, b):
    return not bool(a and b) and not bool(not a and not b)


def fixed_point(x):
    if bool(x) == x:
        return True

    raise ValueError
