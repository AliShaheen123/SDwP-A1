from io import StringIO
import logging
import datetime

file_name = '../output_file.txt'
log_file = '../logs.txt'


def decorator_5(fun):
    import time
    import sys
    import os

    def wrapper(*args, **kwargs):
        wrapper.count += 1
        old_stdout = sys.stdout
        sys.stdout = open(os.devnull, "w")
        st = time.time()
        try:
            fun(*args, **kwargs)
        except Exception:
            old_stderr = sys.stderr
            sys.stderr = open(log_file, 'a')
            logger = logging.getLogger()
            logger.exception(str(datetime.datetime.now()))
            sys.stderr = old_stderr

        end = time.time()
        sys.stdout = old_stdout
        duration = end - st
        print(fun.__name__, 'call', wrapper.count, 'executed in', "{:.7f}".format(duration), 'sec')

    wrapper.count = 0
    return wrapper


def decorator_6(fun):
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
        try:
            fun(*args, **kwargs)
        except Exception:
            old_stderr = sys.stderr
            sys.stderr = open(log_file, 'a')
            logger = logging.getLogger()
            logger.exception(str(datetime.datetime.now()))
            sys.stderr = old_stderr
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


class Decorator7:
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
        try:
            self.func(*args, **kwargs)
        except Exception as e:
            old_stderr = sys.stderr
            sys.stderr = open(log_file, 'a')
            logger = logging.getLogger()
            logger.exception(str(datetime.datetime.now()))
            sys.stderr = old_stderr
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


class Decorator8:
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
        try:
            self.func(*args, **kwargs)
        except Exception as e:
            old_stderr = sys.stderr
            sys.stderr = open(log_file, 'a')
            logger = logging.getLogger()
            logger.exception(str(datetime.datetime.now()))
            sys.stderr = old_stderr
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

