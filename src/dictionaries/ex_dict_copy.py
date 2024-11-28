class DictUtils:
    def my_dict_copy(self, d: dict) -> dict:
        """
        Return a copy of a list or dictionary (only one level)
        :param d: a dict or list to be copied
        :return: new dict as a copy
        """
        c = {}
        if type(d) is dict:
            for key, value in d.items():
                if type(value) in (list, dict):
                    c[key] = value.copy()
                else:
                    raise AttributeError("Wrong dict value type. Expected dict or list received {}".format(type(value)))
        else:
            raise AttributeError("Wrong argument type. Expected dict, received {}".format(type(d)))
        return c


