# -*- coding: utf-8 -*-

import sys
sys.path.append('.')
from src.decorators.delay import delay
from src.decorators.log import log_time_consuming


@log_time_consuming()
@delay(3)
def delay_sum(a, b):
    return a+b

print("call delay_sum...")
sum = delay_sum(1, 2)
print(sum)
