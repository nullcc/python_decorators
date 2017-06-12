# -*- coding: utf-8 -*-

from datetime import datetime
from functools import wraps


def retry(n):
    """
    最多尝试执行n次函数，成功则停止尝试，超过n次未成功则报错
    :param n:
    :return:
    """
    def decorator(func):
        @wraps(func)
        def wrapped_function(tried=0, *args, **kwargs):
            try:
                tried += 1
                print("try {} times for {}".format(tried, func.__name__))
                result = func(tried, *args, **kwargs)
                return result
            except Exception as e:
                if tried < n:
                    return wrapped_function(tried, *args, **kwargs)
                raise e
        return wrapped_function
    return decorator
