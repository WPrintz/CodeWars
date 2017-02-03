"""
Decorator to calculate the time cost to running a function

"""


def time_check(orig_func):
    from time import clock
    def wrapper(*args, **kwargs):
        t1 = clock()
        result = orig_func(*args, **kwargs)
        print('Func: "{}" runtime = {:.3E}'.format(orig_func.__name__, clock()-t1))
        return result
    return wrapper


# @time_check
# Code goes here
#
# @time_check
# def test_func(n):
#     import time
#     for i in range(n):
#         time.sleep(0.1)
#     print('Finished {} loops'.format(n))
#     return n
# test_func(50)