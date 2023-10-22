import datetime


def validate(date_text: str):
    try:
        datetime.date.fromisoformat(date_text)
    except (TypeError, ValueError) as e:
        raise ValueError("Incorrect date format, should be YYYY-MM-DD")


def main():
    d = input("Enter date in format YYYY-MM-DD: ")
    validate(d)
    current_date = datetime.date.fromisoformat(d)
    print("Year: {year}-{month:02d}-{day:02d}".format(year=current_date.year, month=current_date.month, day=current_date.day))

    d1 = d.split("-")
    print("Date: {year}-{month:02d}-{day:02d}".format(year=d1[0], month=int(d1[1]), day=int(d1[2])))
    print("ok")


if __name__ == '__main__':
    main()
