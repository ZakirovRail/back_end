import time


# def sleep(timeout):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             print('time to sleep')
#             time.sleep(timeout)
#             print('time to calc')
#             r = func(*args, **kwargs)
#             print(f'calc result: {r}')
#             return r
#         return wrapper
#     return decorator
#
#
# @sleep(3)
# def square(x):
#     return x * x
#
#
# square(2)
# ======================================================================================================================

class Sleep():
    def __init__(self, timeout):
        self.timeout = timeout

    def __call__(self, func):

        def decorator(*args, **kwargs):
            print('time to sleep')
            time.sleep(self.timeout)
            print('time to calc')
            r = func(*args, **kwargs)
            print(f'calc result: {r}')
            return r
        return decorator

@Sleep(3)
def square(x):
    return x * x


square(2)
