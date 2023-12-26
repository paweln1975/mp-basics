from datetime import datetime, date


def validate(date_text: str):
    try:
        date.fromisoformat(date_text)
    except (TypeError, ValueError) as e:
        raise ValueError("Incorrect date format, should be YYYY-MM-DD")


def test_formatting_date(d):
    validate(d)
    current_date = date.fromisoformat(d)
    print("Year: {year}-{month:02d}-{day:02d}".format(year=current_date.year, month=current_date.month,
                                                      day=current_date.day))

    d1 = d.split("-")
    print("Date: {year}-{month:02d}-{day:02d}".format(year=d1[0], month=int(d1[1]), day=int(d1[2])))
    print("ok")
    return d


def test_formatting_date2(d):
    current_date = datetime.strptime(d, "%Y-%m-%d").date()
    print("{year}\n{month:02d}\n{day:02d}\n".format(year=current_date.year, month=current_date.month,
                                                    day=current_date.day))


def main():
    d = input("Enter date in format YYYY-MM-DD: ")
    test_formatting_date2(d)


if __name__ == '__main__':
    main()
