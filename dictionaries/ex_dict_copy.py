class DictUtils:
    def my_dict_copy(self, d: dict) -> dict:
        c = {}
        if type(d) is dict:
            for key, value in d.items():
                if type(value) in (list, dict):
                    c[key] = value.copy()
                else:
                    raise TypeError("Wrong dict value type. Expected dict or list received {}".format(type(value)))
        else:
            raise TypeError("Wrong argument type. Expected dict, received {}".format(type(d)))
        return c


