"""
Testing duplicates removal from itarable
>>> import sys; sys.tracebacklimit = 0
>>> input = "Jane Mary Jane Tom Alex Sam Alex Sam"
>>> names = input.split(' ')
>>> output = remove_duplicates(names)
>>> print(output)
Alex
Jane
Mary
Sam
Tom

>>> rgb_p = get_RGB('Purple')
>>> rgb_p
(160, 32, 255)

>>> rgb_y = get_RGB('Yellow')
>>> rgb_y
(255, 224, 32)

"""

colors = {'Purple': {'R': 160, 'G': 32, 'B': 255},
          'Light Blue': {'R': 80, 'G': 208, 'B': 255},
          'Yellow': {'R': 255, 'G': 224, 'B': 32}}

def remove_duplicates(names) -> str:
    unique_names = sorted(set(names))
    return '\n'.join(unique_names)

def get_RGB(color: str) -> tuple[int, int, int]:
    return colors[color]['R'], colors[color]['G'], colors[color]['B']







if __name__ == '__main__':
    import doctest
    doctest.testmod()