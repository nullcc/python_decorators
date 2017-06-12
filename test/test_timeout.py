# -*- coding: utf-8 -*-

import sys
sys.path.append('.')
from src.decorators.delay import delay
from src.decorators.timeout import time_out


@time_out(3)
@delay(3.1)
def delay_sum(a, b):
    return a+b

print('start...')
sum = delay_sum(1, 4)
print(sum)
print('end...')
