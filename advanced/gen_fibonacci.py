def gen_fib():
    a, b = 0, 1
    while 1:
        yield b
        a, b = b, a + b


class Fibonacci:

    def __init__(self):
        self.result_map = {1: 0, 2: 1}

    def get(self, n):
        if not n > 0:
            raise ValueError("Param value must be 0 or positive")

        if not self.result_map.get(n) is None:
            return self.result_map[n]

        val = 0
        gen_f = gen_fib()

        for _ in range(n-1):
            val = next(gen_f)

        self.result_map[n] = val

        return val
