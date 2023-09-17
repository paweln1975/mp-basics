class Interview:

    def __init__(self, alternate_alg=False):
        self.input_list = []
        self.alternate_alg = alternate_alg

    def add_one(self, input_list: list[int]) -> list[int]:
        if not self.validate(input_list):
            raise ValueError("Negative or greater then 10 elements are not allowed.")

        return self.__add_one__(input_list) if not self.alternate_alg else self.__add_one_str__(input_list)

    @staticmethod
    def validate(input_list: list[int]) -> bool:
        if len(input_list) > 0 and input_list[0] == 0:
            return False
        return all([0 <= item <= 9 for item in input_list])

    def __add__(self, n, value) -> tuple[int, int]:
        return (1, n + value - 10) if n + value >= 10 else (0, n + value)

    def __add_one__(self, input_list: list[int]) -> list[int]:

        t1 = 1
        l2 = []
        for e in input_list[::-1]:
            t1, t0 = self.__add__(e, t1)
            l2.append(t0)
        if t1:
            l2.append(t1)
        l2.reverse()
        return l2

    def __add_one_ola__(self, input_list: list[int]) -> list[int]:
        if input_list[-1] != 9:
            input_list[-1] += 1
            return input_list
        else:
            input_list[-1] = 0
            self.__add_one_ola__(input_list[:-1])

        return input_list

    def __add_one_alt__(self, input_list: list[int]) -> list[int]:
        list_idx = len(input_list)
        if not list_idx:
            return [1]
        for item in input_list[::-1]:
            list_idx -= 1
            if item == 9:
                input_list[list_idx] = 0
            else:
                input_list[list_idx] = item + 1
                break
        if input_list[0] == 0:
            input_list.insert(0, 1)
        return input_list

    def __add_one_str__(self, input_list: list[int]) -> list[int]:
        str_list = [str(item) for item in input_list] or "0"
        num = int("".join(str_list))
        num += 1
        return [int(item) for item in str(num)]
