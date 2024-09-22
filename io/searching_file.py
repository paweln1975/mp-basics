import glob
"""
Write a function which returns a list of files names found in the HDD.
Requirements:
# write validation 
# use python comprehension

>>> import sys; sys.tracebacklimit = 0
>>> files = find_files('io*.py')
>>> files
['io_intro.py']
"""

def find_files(pattern) -> list[str]:
    iter = glob.iglob(pattern, root_dir='.', recursive=True)
    result = [file_ for file_ in iter]
    return result

