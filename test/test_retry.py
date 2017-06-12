# -*- coding: utf-8 -*-

import sys
sys.path.append('.')
from src.decorators.retry import retry


@retry(5)
def do_something(count, a, b):
    if count < 5:
        count += 1
        raise Exception('Failed!')
    return a + b

res = do_something(0, 1, 4)
print(res)
