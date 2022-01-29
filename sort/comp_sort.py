import timeit
import bubble


def test1():
    list1 = list(reversed(range(100)))
    bubble.bubble_sort(list1)


def test2():
    list1 = list(reversed(range(100)))
    list1.sort()


c = 1000
res_b = timeit.timeit(test1, number=c)
res_s = timeit.timeit(test2, number=c)
print(f"Bubble: {res_b}")
print(f"Built-in: {res_s}")
