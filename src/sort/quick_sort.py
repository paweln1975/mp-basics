def quick_sort(array):
    if len(array) < 2:
        return array
    pivot = array[0]
    left = [x for x in array[1:] if x <= pivot]
    right = [x for x in array[1:] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)


if __name__ == "__main__":
    print(quick_sort([3, 2, 1]))
