def bubble_sort(data: list) -> None:
    n = len(data)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                swapped = True
        if not swapped:
            break


if __name__ == "__main__":
    list1 = list(reversed(range(100)))
    bubble_sort(list1)
    print(list1)

