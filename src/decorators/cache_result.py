# -*- coding: utf-8 -*-

from datetime import datetime
from functools import wraps


def cache_result():
    """
    缓存结果
    :return:
    """
    def decorator(func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            if hasattr(func, "__result"):
                return func.__dict__['__result']
            result = func(*args, **kwargs)
            func.__dict__['__result'] = result
            return result
        return wrapped_function
    return decorator
