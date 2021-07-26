def fib(n: int = 1) -> int:
    """
    Return a fibonacci number.

    :param n: Valid `int` higher then 0 (default 1)
    :return: Return `n` th Fibonacci number for positive parameter.
    :raises ValueError: If input parameter is lower then 1.
    """
    if n < 1:
        raise ValueError("Parameter must higher then 0.")
    prev_val, next_val, ret_value = 0, 1, 1
    for i in range(n - 1):
        ret_value = prev_val + next_val
        prev_val = next_val
        next_val = ret_value
    return ret_value


val_start = 1
for k in range(val_start, val_start + 10):
    print("Fibonacci for {0} equals {1}".format(k, fib(k)))
