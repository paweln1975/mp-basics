def ai_selection_sort(data: list) -> list:
    return [item for i, item in enumerate(data) if i < len(data) - 1 and data[i] < data[i+1]]

