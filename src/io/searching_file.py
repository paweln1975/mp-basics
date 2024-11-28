"""
Use of glob module
"""
import glob

def find_files(pattern) -> list[str]:
    """
    >>> import sys; sys.tracebacklimit = 0
    >>> files = find_files('io*.py')
    >>> files
    ['io_binary.py', 'io_intro.py', 'io_pickle.py', 'io_shelve.py', 'io_write.py']
    """
    iterated_files = glob.iglob(pattern, root_dir='../advanced', recursive=True)
    result = list(iterated_files)
    return result
