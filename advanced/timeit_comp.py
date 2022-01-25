import timeit


def for_loop():
    table1 = []
    for i in range (1, 11):
        for j in range(1, 11):
            table1.append((i, j, i * j))
    return table1


def nested_comp():
    return [(i, j, i*j) for i in range(1, 11) for j in range(1, 11)]


def nested_gen():
    return ([(i, j, i*j) for i in range(1, 11)] for j in range(1, 11))


for_loop_result = timeit.timeit(for_loop, number=50000)
print(f"For loop: {for_loop_result}")

nested_comp_result = timeit.timeit(nested_comp, number=50000)
print(f"Nested comprehension: {nested_comp_result}")

nested_gen_result = timeit.timeit(nested_gen, number=50000)
print(f"Nested generator: {nested_gen_result}")




