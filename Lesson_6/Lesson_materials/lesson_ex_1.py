
# def trace(func):
#     def wrapper(*args, **kwargs):
#         print('start calc')
#         r = func(*args, **kwargs)
#         print(f'calc finished: {r}')
#         return r
#     return wrapper
#
#
# @trace
# def square(x):
#     return x * x
#
#
# square(2)
"""
start calc
calc finished: 4
"""


# ======================================================================================================================


# class Trace:
#
#     def __init__(self):
#         pass
#
#     def __call__(self, func):
#         def some_func(*args, **kwargs):
#             print('start calc from class decorator')
#             r = func(*args, **kwargs)
#             print(f'start calc, result {r}')
#             return r
#         return some_func
#
#
# @Trace()
# def square(x):
#     return x * x
#
#
# square(2)
"""
start calc from class decorator
start calc, result 4
"""
# ======================================================================================================================


def log(func):
    def wrapper(*args, **kwargs):
        print('user start calculations')
        r = func(*args, **kwargs)
        print(f'calc finished: {r}')
        return r
    return wrapper


def trace(func):
    def wrapper(*args, **kwargs):
        print('[start calc]')
        r = func(*args, **kwargs)
        print(f'[calc finished: {r}]')
        return r
    return wrapper


@log
@trace
def square(x):
    return x * x


square(2)



