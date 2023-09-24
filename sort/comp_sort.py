import timeit
import bubble
import selection

SIZE = 250


def test_bubble():
    list1 = list(reversed(range(SIZE)))
    bubble.bubble_sort(list1)


def test_built_in():
    list1 = list(reversed(range(SIZE)))
    list1.sort()


def test_selection():
    list1 = list(reversed(range(SIZE)))
    selection.selection_sort(list1)


c = 100
res = timeit.timeit(test_bubble, number=c)
print("Bubble: {:>12.5f}".format(res))

res = timeit.timeit(test_selection, number=c)
print("Selection: {:>9.5f}".format(res))

res = timeit.timeit(test_built_in, number=c)
print("Built-in: {:>10.5f}".format(res))
