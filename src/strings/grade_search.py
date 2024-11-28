def calc_proportion(input_str: str, grade: str) -> float:
    if len(grade) != 1:
        raise ValueError("Grade must be 1 character long")
    grade_list = input_str.split(' ')
    filtered_list = list(filter(lambda x: x == 'A', grade_list))

    return round(len(filtered_list) / len(grade_list), 2)

