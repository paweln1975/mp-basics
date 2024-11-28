def selection_sort(input_data: list) -> list:
    data_new = []
    data = input_data.copy()
    while data:
        index_min = 0
        item_min = data[index_min]
        index = 0
        for item in data:
            if item < item_min:
                item_min = item
                index_min = index
            index += 1
        data_new.append(data.pop(index_min))
    return data_new


if __name__ == "__main__":
    list1 = list(reversed(range(100)))
    print(selection_sort(list1))


