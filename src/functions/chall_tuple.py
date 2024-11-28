def build_tuple(*args):
    return build_tuple_optimal(args)


def build_tuple_my(args):
    arg_list = []
    for item in args:
        arg_list.append(item)
    return tuple(arg_list)


def build_tuple_optimal(args):
    return args


message_tuple = build_tuple("hello", "world")
print(type(message_tuple))
print(message_tuple)

number_tuple = build_tuple(1, 2, 3)
print(type(number_tuple))
print(number_tuple)