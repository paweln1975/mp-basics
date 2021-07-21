def multiply(x, y):
    result = x * y
    return result


def is_palindrome(word):
    word_forward = word.lower()
    word_backward = word_forward[::-1]
    return word_forward == word_backward


def is_palindrome_sentence(word):
    clean_word = ""
    for char in word:
        if char.isalpha():
            clean_word += char
    print(clean_word)
    return is_palindrome(clean_word)


print(multiply(10, 20))
print(multiply(5, 2.1))

print(is_palindrome("Oko"))

print(is_palindrome_sentence("o k*&# ^^!o"))
print(is_palindrome_sentence("do gees see god?"))
