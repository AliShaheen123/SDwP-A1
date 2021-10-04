
def decorator_1(fun):
    import time
    import sys
    import os

    def wrapper(*args, **kwargs):
        wrapper.count += 1
        old_stdout = sys.stdout
        sys.stdout = open(os.devnull, "w")
        st = time.time()
        fun(*args, **kwargs)
        end = time.time()
        sys.stdout = old_stdout
        duration = end - st
        print(fun.__name__, 'call', wrapper.count, 'executed in', "{:.7f}".format(duration), 'sec')

    wrapper.count = 0
    return wrapper
