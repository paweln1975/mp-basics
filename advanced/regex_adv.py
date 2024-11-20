"""
Regular expression more functions
>>> import sys; sys.tracebacklimit = 0
>>> import re

>>> string = '3 apples, 2 bananas, 5 pears, 10 strawberries'
>>> exp = '(\d+) (\w+)'
>>> result = regexp_find_all(exp, string)
>>> result
[('3', 'apples'), ('2', 'bananas'), ('5', 'pears'), ('10', 'strawberries')]

>>> string = 'blue jeans, white shirt, yellow socks'
>>> exp = '(blue|white|yellow)'
>>> text = 'black'
>>> regexp_replace(exp, string, text)
'black jeans, black shirt, black socks'

>>> text = anonimize('@some_twitter_user I love dogs, @another_twitter_user!')
>>> print(text)
<AUTHOR> I love dogs, <HANDLE>!

>>> string = 'JetBrains Academy'
>>> template_pos = 'JetBrains (?=Academy)'
>>> template_neg = 'JetBrains (?!Academy)'
>>> regexp_match(template_pos, string)
True

>>> regexp_match(template_neg, string)
False

>>> string = 'JetBrains Academy'
>>> template_pos = '(<=JetBrains )Academy'
>>> template_neg = '(<!JetBrains )Academy'

>>> regexp_search(template_neg, string)
False

>>> print(calculate_sum('2 meals $20, groceries $120, 1 month rent $500'))
This week you have spent: 660 dollars

>>> print(calculate_sum('5 meals $1, groceries $30, 1 month rent $100, 5 tickets to ride $20'))
This week you have spent: 235 dollars

>>> string = '<li>Sister</li> <li>Father</li> <li>Mother-in-law</li>'
>>> print(extract_html_li(string))
Sister
Father
Mother-in-law
None
"""
import re
from re import template


def regexp_find_all(template, string) -> list:
    match = re.findall(template, string)
    return match

def regexp_replace(template, string, replacement) -> str:
    result = re.sub(template, replacement, string)
    return result

def anonimize(string) -> str:
    start_text = '<AUTHOR>'
    other_text = '<HANDLE>'

    template = '^@[\w_]*'

    new_text = re.sub(template, start_text, string)

    template = '@[\w_]*'
    new_text = re.sub(template, other_text, new_text)
    return new_text

def regexp_match(template, string) -> bool:
    return re.match(template, string) is not None

def regexp_search(template, string) -> bool:
    return re.search(template, string) is not None

def calculate_sum(string: str) -> str:
    template = ' ?(\d*)? [\w\s]+ \$(\d+),?'
    groups = re.findall(template, string)
    result = 0
    for c, value in groups:
        result += int(c) * int(value) if c is not '' else int(value)
    return f'This week you have spent: {result} dollars'

def extract_html_li(string):
    template = '(?<=<li>)(.*?)(?=<\/li>)'
    groups = re.findall(template, string)
    for group in groups:
        print(group)