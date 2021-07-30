import cProfile
import pstats

pr = cProfile.Profile()
pr.enable()

guard = 9000000

dict1 = {item: item for item in range(10000000)}

new_d = {key: value for key, value in dict1.items() if key >= guard}


def del_iter(d, guard_condition):
    for key, value in list(d.items()):
        if key < guard_condition:
            del d[key]


del_iter(dict1, guard)

pr.disable()

ps = pstats.Stats(pr).sort_stats('cumulative')
ps.print_stats()

print("Items left {}".format(len(dict1)))
print("Items left {}".format(len(new_d)))


