# -*- coding: utf-8 -*-

from functools import wraps
from ..lib.custom_timer import CustomTimer


def delay(seconds):
    """
    延迟执行函数
    :param seconds:
    :return:
    """
    def decorator(func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            ct = CustomTimer(seconds, func, *args, **kwargs)
            ct.start()
            return ct.c_join()
        return wrapped_function
    return decorator
