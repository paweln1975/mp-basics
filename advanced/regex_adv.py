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
"""
import re

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