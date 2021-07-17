def multiply(x, y):
    result = x * y
    return result


def is_palindrome(word):
    word_forward = word.lower()
    word_backward = word_forward[::-1]
    return word_forward == word_backward


print(multiply(10, 20))
print(multiply(5, 2.1))

print(is_palindrome("Oko"))
