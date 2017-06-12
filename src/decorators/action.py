# -*- coding: utf-8 -*-

from functools import wraps


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
