def multiply(x, y):
    result = x * y
    return result


def is_palindrome(word):
    """
    Check if a string is a palindrome.

    A palindrome is a string that reads the same forwards as backwards.

    :param word: The string to check.
    :return: True if `string` is a palindrome, False otherwise.
    """
    word_forward = word.lower()
    word_backward = word_forward[::-1]
    return word_forward == word_backward


def is_palindrome_sentence(word):
    """
    Check if a sentence is a palindrome.

    The function ignores whitespace, capitalisation and
    punctuation in the sentence.
 
    :param word: The sentence to check.
    :return: True if `sentence` is a palindrome, False otherwise.
    """
    clean_word = ""
    for char in word:
        if char.isalpha():
            clean_word += char
    print(clean_word)
    return is_palindrome(clean_word)


def center_text(*args):
    for arg in args:
        t = str(arg)
        left_margin = (80 - len(t)) // 2
        print(" " * left_margin, t)


center_text("Michael Jordan")
center_text("23")
center_text("Chicago Bulls")

center_text("AAA", "BBB", "CCC")

print(multiply(10, 20))
print(multiply(5, 2.1))

print(is_palindrome("Oko"))

print(is_palindrome_sentence("o k*&# ^^!o"))
print(is_palindrome_sentence("do gees see god?"))
