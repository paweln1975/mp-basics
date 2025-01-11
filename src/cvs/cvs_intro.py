"""
cvs library training
>>> import sys; sys.tracebacklimit = 0
>>> output = count_sprits('available-for-consumption-year-ended-december-2019-csv.csv', 'MAGNITUDE')
>>> print(output)
3747

>>> filename = "criminals.csv"
>>> write_to_csv(filename)
>>> output = read_from_csv(filename)
>>> output
3
"""
import csv

def count_sprits(filename, value):
    with open(filename) as f:
        file_reader = csv.DictReader(f, delimiter=',')
        count = 0
        for row in file_reader:
            if row[value] == '0':
                count += 1
    f.close()
    return count


def write_to_csv(filename):
    with open(filename, "w", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter=",", lineterminator="\n")
        file_writer.writerow(["Name", "Age", "Height"])
        file_writer.writerow(["Alex", "23", "184"])
        file_writer.writerow(["Karla", "35", "170"])
        file_writer.writerow(["Tim", "21", "178"])
    w_file.close()


def read_from_csv(filename):
    count = 0
    with open(filename, newline='') as crime:
        file_reader = csv.reader(crime, delimiter=",")  # Create a reader object
        for _ in file_reader:  # Read each line
            count += 1
    return count - 1