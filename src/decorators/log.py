# -*- coding: utf-8 -*-

from datetime import datetime
from functools import wraps


def log_time_consuming():
    """
    记录函数执行时间
    :return:
    """
    def decorator(func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            start = datetime.now()
            result = func(*args, **kwargs)
            end = datetime.now()
            print("function {} consums {} seconds".format(func.__name__, end - start))
            return result
        return wrapped_function
    return decorator
