# -*- coding: utf-8 -*-

from functools import wraps
from ..lib.custom_timer import CustomTimer


def before_action(before):
    """
    在函数运行前运行指定函数
    :param before:
    :return:
    """
    def decorator(func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            before()
            result = func(*args, **kwargs)
            return result
        return wrapped_function
    return decorator


def after_action(after):
    """
    在函数运行后运行指定函数
    :param after:
    :return:
    """
    def decorator(func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            result = func(*args, **kwargs)
            after()
            return result
        return wrapped_function
    return decorator


def around_action(before, after):
    """
    在函数运行前后运行指定函数
    :param before:
    :param after:
    :return:
    """
    def decorator(func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            before()
            result = func(*args, **kwargs)
            after()
            return result
        return wrapped_function
    return decorator


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
