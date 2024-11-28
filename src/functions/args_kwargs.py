def fun_args(*args):
    print(f'Type of args: {type(args)}')
    print(f'Value of args: {args}')
    i = 0
    for x in args:
        i += 1
        print(f'Param {i} value={x}')


def fun_kwargs(**kwargs):
    print(f'Type of args: {type(kwargs)}')
    print(f'Value of args: {kwargs}')
    i = 0
    for k, x in kwargs.items():
        i += 1
        print(f'Param {i} key={k} value={x}')


print('1. ' + '#' * 50)
fun_args(1, 2, 3, 4, 5)
print('2. ' + '#' * 50)
fun_args((1, 2, 3, 4, 5))
print('3. ' + '#' * 50)
fun_args(*(1, 2, 3, 4, 5))

print('4. ' + '#' * 50)
fun_kwargs(a=1, b=2, c=3)
print('5. ' + '#' * 50)
d = {'a': 1, 'b': 2, 'c': 3}
fun_kwargs(**d)
