# import time
#
#
# def timing(func):
#     def wrapper(*args, **kwargs):
#         time.sleep(1)
#         r = func(*args, **kwargs)
#         print(f'new call for {r}')
#         return r
#     return wrapper
#
#
# @timing
# def factorial(n):
#     if n <= 1:
#         return 1
#     else:
#         return n * factorial(n-1)
#
# print(factorial(5))
# ======================================================================================================================
from datetime import datetime


# def timing(func):
#     def wrapper(*args, **kwargs):
#         t1 = datetime.now()
#         r = func(*args, **kwargs)
#         t2 = datetime.now()
#         print(f'{t2.microsecond - t1.microsecond} microseconds')
#         return r
#     return wrapper
#
# @timing
# def fibonacci(n):
#     if n == 1 or n == 2:
#         return 1
#     return fibonacci(n - 1) * fibonacci(n - 2)

# fibonacci(5)
"""
1 seconds
2 seconds
33 seconds
1 seconds
43 seconds
0 seconds
1 seconds
9 seconds
67 seconds
"""


# ======================================================================================================================
from datetime import datetime


def timing(func):
    def wrapper(*args, **kwargs):
        t1 = datetime.now()
        r = func(*args, **kwargs)
        t2 = datetime.now()
        print(f'{t2.microsecond - t1.microsecond} microseconds')
        return r
    return wrapper


def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) * fibonacci(n - 2)


timing(fibonacci)(5)  # in case def fibonacci without decorator - only once result will be shown 12 microseconds



