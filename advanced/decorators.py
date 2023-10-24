def tagged(fun_name):
    def wrapper(s: str):
        s2 = fun_name(s)
        return '<title>' + s2 + '</title>'

    return wrapper


@tagged
def from_input(inp):
    string = inp.strip()
    return string


def price_string(func):
    def wrapper(quantity):
        return "£" + str(func(quantity))

    return wrapper


@price_string
def new_price(old_price: float) -> float:
    return 0.9 * old_price


print(from_input(" Test "))
print(new_price(100))
