"""
Regular expression introduction
>>> import sys; sys.tracebacklimit = 0
>>> import re
>>> input = "Where is?"
>>> output = simple_check(input, ".here is.?")
>>> output
True

>>> re.match('/?', '?') is not None
True

"""
import re
import sys


def simple_check(s: str, pattern: str) -> bool:
    return re.match(pattern, s) is not None

def group_find_all(s: str, pattern: str) -> list[str]:
    return re.findall(pattern, s)

def find_date(s: str) -> list[str]:
    """
    >>> output_date = find_date('1975-05-30')
    >>> output_date
    [('1975', '05', '30')]
    """
    return group_find_all(s, r"(\d{4})-(\d{2})-(\d{2})")

def check_name(s: str) -> bool:
    """
    Checks if start with any letter from B to N
    And the second character has to be a vowel.
    Rest of the string could by any.
    Returns Suitable! if match.
    >>> check_name('Butterfly')
    'Suitable!'
    """
    pattern = '[B-N][aeuyio].?+'
    return 'Suitable!' if simple_check(s, pattern) else False

def check_hyphened_word(s: str) -> bool:
    """
    >>> check_hyphened_word('twenty-one')
    True

    >>> check_hyphened_word('noone')
    False
    """
    return simple_check(s, r"[a-z]+-[a-z]+")

def check_smith_person(s: str) -> bool:
    """
    >>> check_smith_person('Anna Smith')
    True

    >>> check_smith_person('Anna Nicole Smith')
    True

    >>> check_smith_person('Anna NicoleSmith')
    False

    >>> check_smith_person('anna Smith')
    False
    """
    template = r"([A-Z][a-z]+\s){1,}Smith$"
    return simple_check(s, template)

def check_definite_article(s: str) -> bool:
    """
    >>> check_definite_article('the')
    True

    >>> check_definite_article('theft')
    False
    """
    template = r'^the$'
    return simple_check(s, template)

def check_india_plate_pattern(s: str) -> bool:
    """
    >>> check_india_plate_pattern('MH 10 EL 531114')
    False

    >>> check_india_plate_pattern('MH 10 EL 5311')
    True
    """
    template = "^[A-Z]{2} *[0-9]{2} *[A-Z]{2} *[0-9]{4}$"
    return simple_check(s, template)

def check_python_version() -> tuple[int, int]:
    """
    >>> check_python_version()
    (3, 12)
    """
    version = sys.version
    pattern = r"([0-9]{1})\.(\d{1,})"
    match_1 = re.match(pattern, version)
    return int(match_1.group(1)), int(match_1.group(2))

def check_email(email: str) -> bool:
    """
    Its first part can contain from 6 to 30 characters.
    These characters can contain lowercase Latin letters (a-z), digits (0-9),
    hyphens -, dot characters . , equal signs = or underscores _
    The second part that immediately follows the first one can be either @gmail.com,
    @jetbrains.org or @hyperskill.org
    Note that other combinations of the correct domain and top-level domain names are invalid. For example, @jetbrains.com or @gmail.org shouldn't be accepted by your regex.
    >>> check_email('<EMAIL>')
    False
    >>> check_email('pawel.niedziela@gmail.com')
    True
    """
    template = r"^[a-z0-9_=\-.]{6,30}@(?:gmail\.com|jetbrains\.org|hyperskill\.org)$"
    return simple_check(email, template)