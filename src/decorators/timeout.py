# -*- coding: utf-8 -*-

from functools import wraps
from ..lib.custom_timer import CustomTimer


def time_out(seconds):
    """
    设置超时时间，如果超时则抛出异常
    :param seconds:
    :return:
    """
    def decorator(func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            def time_out_func():
                raise Exception('Time out.')
            ct = CustomTimer(seconds, time_out_func)
            ct.start()
            result = func(*args, **kwargs)
            ct.cancel()
            return result
        return wrapped_function
    return decorator
