import time


def timer(func):
    def inner_func(*args, **kwargs):
        now = time.time()
        results = func(*args, **kwargs)
        print('Function took {} to run.'.format(time.time() - now))
        return results
    return inner_func
