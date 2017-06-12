# -*- coding: utf-8 -*-

import sys
sys.path.append('.')
from src.decorators.action import (before_action, after_action, around_action)


def before_say():
    print('before_say')


def after_say():
    print('after_say')


@before_action(before_say)
def say_before():
    print('say')


@after_action(after_say)
def say_after():
    print('say')


@around_action(before_say, after_say)
def say_around():
    print('say')

say_before()

print('======')

say_after()

print('======')

say_around()

print('======')