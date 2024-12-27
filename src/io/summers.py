"""
summers cout library training
>>> import sys; sys.tracebacklimit = 0
>>> count = count_word_in_file('summers.txt', 'summer')
>>> count
3
>>> count = count_word_in_file('hyperskill-dataset.txt', 'summer')
>>> count
9
"""

def count_word_in_file(filename, word) -> int:
    with open(filename, mode='r', encoding='utf-8') as f:
        content = f.read()
    word_list = content.split()
    return word_list.count(word)


def print_sums():
    with open('sums.txt') as f:
        for line in f:
            print(sum(map(int, line.split())))
    f.close()
