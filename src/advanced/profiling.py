import cProfile
import time
from timeit_comp import for_loop, nested_comp

profile = cProfile.Profile()
profile.enable()

for i in range(100):
    for_loop()
    nested_comp()

profile.disable()
profile.print_stats()

