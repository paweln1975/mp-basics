def sum_eo(n, t):
    if t == 'e':
        r1 = range(2, n, 2)
    elif t == 'o':
        r1 = range(1, n, 2)
    else:
        return -1

    return sum(r1)


print(sum_eo(10, 'e'))
print(sum_eo(10, 'o'))
