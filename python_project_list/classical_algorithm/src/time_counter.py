def count_time(f):
    import time
    def time_decorator(*args, **kwargs):
        t = time.clock()
        res = f(*args, **kwargs)
        print (f.__name__, time.clock() - t)
        return res
    return time_decorator