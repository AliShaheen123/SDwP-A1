from io import StringIO


class NullIO(StringIO):

    def __init__(self):
        super().__init__()
        self.value = ''

    def write(self, txt):
        self.value += txt


def decorator_2(fun):
    import time
    import sys
    from inspect import signature, getsource
    if not fun.__doc__:
        print(f"Error: the function {fun.__name__} does not have a docstring.", end=' ')
        print("No decoration or attachment is done with function decorator 'decorator_2'.")
        return fun

    def wrapper(*args, **kwargs):
        wrapper.count += 1
        old_stdout = sys.stdout
        sys.stdout = NullIO()
        st = time.time()
        fun(*args, **kwargs)
        end = time.time()
        output = sys.stdout.value
        sys.stdout = old_stdout
        duration = end - st
        out_dict = {
            'Name': fun.__name__,
            'Type': type(fun),
            'Sign': signature(fun),
            'Args': f'positional {args}\n      key=worded {kwargs}',
            'Doc': fun.__doc__,
            'Source': getsource(fun),
            'output': output
        }
        print(fun.__name__, 'call', wrapper.count, 'executed in', "{:.7f}".format(duration), 'sec')

        for key, val in out_dict.items():
            print(f"{key}: {val}")

    wrapper.count = 0
    return wrapper
