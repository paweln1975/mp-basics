"""
Testing default dict
>>> import sys; sys.tracebacklimit = 0

>>> d1 = {}
>>> k = 10
>>> add_value_to_dict(d1, 'k', k)
10
>>> d1
{'k': 10}
>>> add_value_to_dict(d1, 'k', k)
20
>>> d1
{'k': 20}
>>> value = d1.get('k1', 0)
>>> value
0

>>> text = "Hello, world! welcome to the world of Python. Hello again; welcome"
>>> freq_dict = create_freq_dict(text)
>>> freq_dict
{'hello': 2, 'world': 2, 'welcome': 2, 'to': 1, 'the': 1, 'of': 1, 'python': 1, 'again': 1}

>>> from collections import Counter
>>> counter = Counter(text.lower().split())
>>> counter.most_common(1)
[('welcome', 2)]

>>> counter.total()
11

>>> import lorem
>>> lorem_generator = TextLorem(trange=(100, 300))
>>> text = lorem_generator.text()

>>> result = create_default_freq_dict(text)
>>> result["bajabongo"]
0
"""

import lorem
from lorem.text import TextLorem
from collections import defaultdict, Counter

from list import result


def add_value_to_dict(data: dict, key: str, value: int):
    """
    setdefault method gets the value from dictionary, if the value for the key does not
    exist it sets the default value.
    """
    data[key] = data.setdefault(key, 0) + value
    return data[key]


def create_freq_dict(text: str) -> dict:
    """
    Method takes a text as an argument, removes commas, dots, colons and semicolons.
    Creates a dict with a use of setdefault method. For each word in the text the method
    add a new entry in the frequency dict with the value of number of word occurence number.
    It returns the new dict.
    """
    for char in ",.:;!":
        text = text.replace(char, '')

    text = text.lower()

    freq_dict = {}
    words = text.split()

    for word in words:
        freq_dict.setdefault(word, 0)
        freq_dict[word] += 1

    return freq_dict

def create_default_freq_dict(text: str) -> dict:
    freq_dict = defaultdict(int)
    words = text.split()

    for word in words:
        freq_dict[word] += 1

    return freq_dict


def _hyperskill_challange_one():
    """
    >>> transaction_dict = _hyperskill_challange_one()
    >>> transaction_dict
    {38177: [34.38, 876.75], 876: [999.99, 3456, 98.7], 654276: [653678, 0.55], 54366: [0.99], 546: [987.65]}
    """

    transactions = [(38177, 34.38), (876, 999.99), (654276, 653678), (54366, 0.99),
                    (546, 987.65), (876, 3456), (654276, 0.55), (38177, 876.75), (876, 98.7)]
    result_dict = {}
    for account, amount in transactions:
        result_dict.setdefault(account, []).append(amount)
    return result_dict


def _hyperskill_challange_two(data):
    """
    In statistics, the mode is the most common value in the data.

    The input format:
        The data values separated by whitespace. The data can be of any type: numbers, words, etc. It is guaranteed
        that the data will have only one mode!

    The output format:
        The mode of the data.

    >>> data = '1 7 3 3 8 9 10 5 5 5 4 1 5 6'
    >>> mode = _hyperskill_challange_two(data)
    >>> mode
    '5'

    >>> data='red green yellow red orange blue purple'
    >>> mode = _hyperskill_challange_two(data)
    >>> mode
    'red'
    """
    data = data.split(' ')
    counter = Counter(data)
    return counter.most_common(1)[0][0]

if __name__ == '__main__':
    import doctest
    doctest.testmod()