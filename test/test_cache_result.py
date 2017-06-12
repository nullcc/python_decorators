# -*- coding: utf-8 -*-

import sys
sys.path.append('.')
from src.decorators.cache_result import cache_result


@cache_result()
def complex_calculation():
    print('run complex_calculation!')
    return 2

res1 = complex_calculation()
res2 = complex_calculation()
res3 = complex_calculation()
print(res1)
print(res2)
print(res3)
