import timeit


for_loop = """
table1 = []
for i in range (1, 11):
    for j in range(1, 11):
        table1.append((i, j, i * j))
#        print(f"{i} * {j} = {i * j}")
"""

nested_comp = """
table2 = [(i, j, i*j) for i in range(1, 11) for j in range(1, 11)]
"""

for_loop_result = timeit.timeit(for_loop, number=500000)
print(f"For loop: {for_loop_result}")

nested_comp_result = timeit.timeit(nested_comp, number=500000)
print(f"Nested comprehension: {nested_comp_result}")

