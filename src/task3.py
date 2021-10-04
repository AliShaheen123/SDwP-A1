from io import StringIO

file_name = '../output_file.txt'


class Decorator3:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        import time
        import sys
        import os

        self.count += 1
        old_stdout = sys.stdout
        sys.stdout = open(os.devnull, "w")
        st = time.time()
        self.func(*args)
        end = time.time()
        sys.stdout = old_stdout
        duration = end - st
        file = open(file_name, 'a')
        file.write(f"{self.func.__name__} call {self.count} executed in " + "{:.7f} ".format(duration) + 'sec\n')
        file.close()


class NullIO(StringIO):

    def __init__(self):
        super().__init__()
        self.value = ''

    def write(self, txt):
        self.value += txt


class Decorator4:
    def __init__(self, func):
        self.func = func
        self.count = 0
        if not func.__doc__:
            file = open(file_name, 'a')
            file.write(f"Error: the function {func.__name__} does not have a docstring. ")
            file.write("No decoration or attachment is done with function decorator 'decorator_2'.\n")

    def __call__(self, *args, **kwargs):
        if not self.func.__doc__:
            return self.func(*args, **kwargs)

        import time
        import sys
        from inspect import signature, getsource

        self.count += 1
        old_stdout = sys.stdout
        sys.stdout = NullIO()
        st = time.time()
        self.func(*args, **kwargs)
        end = time.time()
        output = sys.stdout.value
        sys.stdout = old_stdout
        duration = end - st

        out_dict = {
            'Name': self.func.__name__,
            'Type': type(self.func),
            'Sign': signature(self.func),
            'Args': f'positional {args}\n      key=worded {kwargs}',
            'Doc': self.func.__doc__,
            'Source': getsource(self.func),
            'output': output
        }

        file = open(file_name, 'a')
        file.write(f"{self.func.__name__} call {self.count} executed in " + "{:.7f} ".format(duration) + 'sec\n')

        for key, val in out_dict.items():
            file.write(f"{key}: {val}\n")
        file.close()

