import sys
sys.path.append('.')
from src.decorators.decorators import (before_action, after_action, around_action, delay, time_out)


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
print('====')
say_after()
print('====')
say_around()


print('start...')


@delay(3)
def delay_sum(a, b):
    return a+b


@delay(3)
def delay_say():
    return 'say'

print(delay_sum(1, 3))
print(delay_say())

print('end...')


@time_out(3)
@delay(2.9)
def delay_sum(a, b):
    return a+b

print('start...')
print(delay_sum(1, 4))
print('end...')
