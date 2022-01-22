for i in range (1, 11):
    for j in range(1, 11):
        print(f"{i} * {j} = {i * j}")

for t1, t2, r in [(i, j, i*j) for i in range(1, 11) for j in range(1, 11)]:
    print(f"{t1} * {t2} = {r}")
